"""Dashboard catalog and detail views."""

from flask import Blueprint, render_template

bp = Blueprint("dashboards", __name__, url_prefix="/dashboards")


@bp.get("/")
def catalog():
    """List available dashboards."""
    return render_template("dashboards/catalog.html")


@bp.get("/<int:dashboard_id>")
def detail(dashboard_id: int):
    """Show dashboard details."""
    return render_template("dashboards/detail.html", dashboard_id=dashboard_id)
