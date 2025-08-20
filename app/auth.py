import secrets
from typing import Dict, Any

import pymysql


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

        # Ensure the bookkeeping table exists
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS user_databases (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                db_name VARCHAR(255) NOT NULL,
                db_user VARCHAR(255) NOT NULL,
                db_password VARCHAR(255) NOT NULL
            );
            """
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
