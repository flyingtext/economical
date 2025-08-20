from __future__ import annotations

import json
from pathlib import Path

from flask import Blueprint, jsonify

bp = Blueprint("data", __name__, url_prefix="/api/data")


@bp.get("/<series_id>")
def get_series(series_id: str):
    """Return a cached time series as JSON."""
    file_path = Path("cache") / f"{series_id}.json"
    if not file_path.exists():
        return jsonify({"error": "Series not found"}), 404
    data = json.loads(file_path.read_text())
    return jsonify(data)
