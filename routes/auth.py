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
import secrets

# Simple in-memory store for registered users
registered_users: list[dict] = []
# In-memory mapping of reset tokens to user emails
reset_tokens: dict[str, str] = {}


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


@bp.route("/password-reset", methods=["GET", "POST"])
def password_reset_request():
    """Handle password reset email requests."""
    error = None
    message = None
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        if not email:
            error = "Email is required"
        elif not any(u["email"] == email for u in registered_users):
            error = "Email not found"
        if error is None:
            token = secrets.token_urlsafe(16)
            reset_tokens[token] = email
            reset_link = url_for("auth.password_reset_token", token=token, _external=True)
            print(f"Password reset link for {email}: {reset_link}")
            message = "If the email exists, a reset link has been sent."
    return render_template("auth/password_reset_request.html", error=error, message=message)


@bp.route("/password-reset/<token>", methods=["GET", "POST"])
def password_reset_token(token: str):
    """Validate reset token and update password."""
    error = None
    if token not in reset_tokens:
        return render_template(
            "auth/password_reset_form.html", error="Invalid or expired token", invalid=True
        ), 400
    if request.method == "POST":
        password = request.form.get("password", "")
        confirm = request.form.get("confirm", "")
        if not password or not confirm:
            error = "All fields are required"
        elif password != confirm:
            error = "Passwords do not match"
        elif not _is_strong_password(password):
            error = "Password too weak"
        if error is None:
            email = reset_tokens.pop(token)
            for user in registered_users:
                if user["email"] == email:
                    user["password"] = password
                    break
            return redirect(url_for("auth.password_reset_success"))
    return render_template("auth/password_reset_form.html", error=error, token=token)


@bp.get("/password-reset/success")
def password_reset_success():
    """Display success message after password reset."""
    return render_template("auth/password_reset_success.html")
