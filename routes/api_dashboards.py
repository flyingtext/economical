from flask import Blueprint, jsonify

bp = Blueprint("api_dashboards", __name__, url_prefix="/api/dashboards")

DASHBOARDS = [
    {"id": 1, "name": "Dashboard 1", "description": "First dashboard"},
    {"id": 2, "name": "Dashboard 2", "description": "Second dashboard"},
]


@bp.get("/")
def list_dashboards():
    """Return all dashboards."""
    return jsonify(DASHBOARDS)


@bp.get("/<int:dashboard_id>")
def dashboard_detail(dashboard_id: int):
    """Return details for a single dashboard."""
    dashboard = next((d for d in DASHBOARDS if d["id"] == dashboard_id), None)
    if dashboard is None:
        return jsonify({"error": "Dashboard not found"}), 404
    return jsonify(dashboard)
