"""Admin dashboard routes."""

from flask import Blueprint, render_template

bp = Blueprint("admin", __name__, url_prefix="/admin")


@bp.get("/")
def dashboard():
    """Render the admin dashboard."""
    return render_template("admin/dashboard.html")
