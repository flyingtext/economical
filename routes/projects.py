"""Project catalog and detail views."""

from flask import Blueprint, render_template

bp = Blueprint("projects", __name__, url_prefix="/projects")


@bp.get("/")
def catalog():
    """List available projects."""
    return render_template("projects/catalog.html")


@bp.get("/<int:project_id>")
def detail(project_id: int):
    """Show project details."""
    return render_template("projects/detail.html", project_id=project_id)
