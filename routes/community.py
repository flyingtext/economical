"""Community feed routes."""

from flask import Blueprint, render_template

bp = Blueprint("community", __name__, url_prefix="/community")


@bp.get("/")
def feed():
    """Render the global community feed."""
    return render_template("community/feed.html")
