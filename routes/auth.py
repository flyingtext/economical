"""Authentication and account related routes."""

from flask import (
    Blueprint,
    render_template,
    redirect,
    request,
    url_for,
    jsonify,
)
import re

# Simple in-memory store for registered users
registered_users: list[dict] = []


def _is_strong_password(password: str) -> bool:
    """Basic password strength check."""
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    return True

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/login", methods=["GET", "POST"])
def login():
    """Render the login page and handle basic login submissions."""
    error = None
    success = request.args.get("success")
    if request.method == "POST":
        email = request.form.get("email", "")
        password = request.form.get("password", "")
        # Placeholder authentication logic. Accept any non-empty credentials.
        if email and password:
            return redirect(url_for("index"))
        error = "Invalid credentials"
        if request.headers.get("X-Requested-With") == "XMLHttpRequest":
            return jsonify({"error": error}), 400
    return render_template("auth/login.html", error=error, success=success)


@bp.route("/signup", methods=["GET", "POST"])
def signup():
    """Render the sign up page and handle registrations."""
    error = None
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        confirm = request.form.get("confirm", "")
        contact = request.form.get("contact", "").strip()
        terms = request.form.get("terms")
        if not all([name, email, password, confirm, contact, terms]):
            error = "All fields are required"
        elif password != confirm:
            error = "Passwords do not match"
        elif not _is_strong_password(password):
            error = "Password too weak"
        elif any(u["email"] == email for u in registered_users):
            error = "Email already registered"
        if error is None:
            registered_users.append(
                {
                    "name": name,
                    "email": email,
                    "password": password,
                    "contact": contact,
                }
            )
            return redirect(url_for("auth.login", success="Account created. Please log in."))
        if request.headers.get("X-Requested-With") == "XMLHttpRequest":
            return jsonify({"error": error}), 400
    return render_template("auth/signup.html", error=error)


@bp.get("/check-email")
def check_email():
    """AJAX endpoint to check for existing email."""
    email = request.args.get("email", "").strip().lower()
    exists = any(u["email"] == email for u in registered_users)
    return jsonify({"exists": exists})


@bp.get("/password-reset")
def password_reset():
    """Render the password reset page."""
    return render_template("auth/password_reset.html")
