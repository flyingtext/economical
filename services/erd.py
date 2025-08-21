from __future__ import annotations

from pathlib import Path
import re
import pymysql

# Map ERD types to MySQL column types
TYPE_MAP = {
    "uuid": "CHAR(36)",
    "string": "VARCHAR(255)",
    "int": "INT",
    "datetime": "DATETIME",
    "json": "JSON",
}


def parse_erd(erd_path: Path) -> dict[str, list[tuple[str, str]]]:
    """Parse a Mermaid ERD file into table definitions.

    Parameters
    ----------
    erd_path:
        Path to the ERD markdown file containing a ``mermaid`` ``erDiagram``.

    Returns
    -------
    dict
        Mapping of table name to list of ``(column_name, sql_type)`` tuples.
    """
    tables: dict[str, list[tuple[str, str]]] = {}
    current_table: str | None = None
    for line in erd_path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("%%"):
            continue
        match = re.match(r"([A-Z_]+) \{", line)
        if match:
            current_table = match.group(1).lower()
            tables[current_table] = []
            continue
        if line == "}" and current_table:
            current_table = None
            continue
        if current_table:
            parts = line.split()
            if len(parts) >= 2:
                col_type, col_name = parts[0], parts[1]
                sql_type = TYPE_MAP.get(col_type.lower(), "TEXT")
                tables[current_table].append((col_name, sql_type))
    return tables


def apply_erd_schema(conn: pymysql.connections.Connection, erd_path: Path) -> None:
    """Create tables defined in the ERD if they do not exist."""
    tables = parse_erd(erd_path)
    with conn.cursor() as cur:
        for table, columns in tables.items():
            col_defs = ",\n".join(f"    {name} {ctype}" for name, ctype in columns)
            sql = f"CREATE TABLE IF NOT EXISTS {table} (\n{col_defs}\n);"
            cur.execute(sql)
    conn.commit()
