from __future__ import annotations

from pathlib import Path

import pymysql


def apply_migrations(conn: pymysql.connections.Connection, migrations_dir: Path) -> None:
    """Apply SQL migrations located in ``migrations_dir``.

    Each ``.sql`` file is executed once and tracked in the ``schema_migrations``
    table. Files are processed in alphabetical order.
    """
    migrations_dir = migrations_dir.resolve()
    with conn.cursor() as cur:
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS schema_migrations (
                version VARCHAR(255) PRIMARY KEY,
                applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """
        )
        cur.execute("SELECT version FROM schema_migrations")
        applied = {row[0] for row in cur.fetchall()}

        for path in sorted(migrations_dir.glob("*.sql")):
            version = path.stem
            if version in applied:
                continue
            statements = [s.strip() for s in path.read_text().split(";") if s.strip()]
            for statement in statements:
                cur.execute(statement)
            cur.execute(
                "INSERT INTO schema_migrations (version) VALUES (%s)",
                (version,),
            )
    conn.commit()
