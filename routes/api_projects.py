from flask import Blueprint, jsonify

bp = Blueprint("api_projects", __name__, url_prefix="/api/projects")

PROJECTS = [
    {"id": 1, "name": "Project 1", "description": "First project"},
    {"id": 2, "name": "Project 2", "description": "Second project"},
]


@bp.get("/")
def list_projects():
    """Return all projects."""
    return jsonify(PROJECTS)


@bp.get("/<int:project_id>")
def project_detail(project_id: int):
    """Return details for a single project."""
    project = next((p for p in PROJECTS if p["id"] == project_id), None)
    if project is None:
        return jsonify({"error": "Project not found"}), 404
    return jsonify(project)
