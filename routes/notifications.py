"""User notification routes."""

from flask import Blueprint, render_template
from ws import emit_notification

bp = Blueprint("notifications", __name__, url_prefix="/notifications")


@bp.get("/")
def list_notifications():
    """List notifications for the current user."""
    emit_notification("notification list accessed")
    return render_template("notifications/list.html")
