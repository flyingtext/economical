"""Authentication and account related routes."""

from flask import Blueprint, render_template

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.get("/login")
def login():
    """Render the login page."""
    return render_template("auth/login.html")


@bp.get("/signup")
def signup():
    """Render the sign up page."""
    return render_template("auth/signup.html")


@bp.get("/password-reset")
def password_reset():
    """Render the password reset page."""
    return render_template("auth/password_reset.html")
