from __future__ import annotations

import secrets
from pathlib import Path
from typing import Dict, Any

import pymysql

from services.migrations import apply_migrations


def register_user_with_database(conn: pymysql.connections.Connection, user_id: int, username: str) -> Dict[str, Any]:
    """Hook executed after user registration.

    This function creates a per-user MySQL database and user, grants the
    necessary privileges and records the generated credentials in the
    ``user_databases`` table.

    Parameters
    ----------
    conn:
        An established :class:`pymysql.Connection` with sufficient
        privileges to create databases and users.
    user_id:
        Identifier of the newly created application user.
    username:
        The username used for application login. This is reused as the
        MySQL user and as the prefix for the database name.

    Returns
    -------
    dict
        A dictionary containing the database name, username and generated
        password for further processing.
    """
    db_name = f"{username}_db"
    db_user = username
    db_password = secrets.token_urlsafe(16)

    migrations_dir = Path(__file__).resolve().parent.parent / "migrations"
    apply_migrations(conn, migrations_dir)

    with conn.cursor() as cur:
        # Create database and user
        cur.execute(f"CREATE DATABASE `{db_name}`;")
        cur.execute(
            "CREATE USER %s@'%%' IDENTIFIED BY %s;",
            (db_user, db_password),
        )

        # Grant privileges to the new user on its database
        cur.execute(
            f"GRANT ALL PRIVILEGES ON `{db_name}`.* TO %s@'%%';",
            (db_user,),
        )

        # Record the generated credentials
        cur.execute(
            """
            INSERT INTO user_databases (user_id, db_name, db_user, db_password)
            VALUES (%s, %s, %s, %s);
            """,
            (user_id, db_name, db_user, db_password),
        )

    conn.commit()
    return {"db_name": db_name, "db_user": db_user, "db_password": db_password}
