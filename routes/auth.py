"""Authentication and account related routes."""

from flask import (
    Blueprint,
    render_template,
    redirect,
    request,
    url_for,
    jsonify,
    session,
)
from datetime import datetime
import re
import secrets
from werkzeug.security import check_password_hash, generate_password_hash

from models.db import SessionLocal
from models.user import User, PasswordResetToken, ActiveSession


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
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        db = SessionLocal()
        user = db.query(User).filter_by(email=email).first()
        if user and check_password_hash(user.password_hash, password):
            session["user_id"] = user.id
            token = secrets.token_urlsafe(16)
            session["session_token"] = token
            db.add(
                ActiveSession(
                    user_id=user.id,
                    token=token,
                    ip=request.remote_addr,
                    login_at=datetime.utcnow(),
                )
            )
            db.commit()
            db.close()
            return redirect(url_for("my_account.dashboard"))
        db.close()
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
        else:
            db = SessionLocal()
            if db.query(User).filter_by(email=email).first():
                error = "Email already registered"
            elif error is None:
                user = User(
                    name=name,
                    email=email,
                    password_hash=generate_password_hash(password),
                    contact=contact,
                )
                db.add(user)
                db.commit()
                db.close()
                return redirect(url_for("auth.login", success="Account created. Please log in."))
            db.close()
        if request.headers.get("X-Requested-With") == "XMLHttpRequest":
            return jsonify({"error": error}), 400
    return render_template("auth/signup.html", error=error)


@bp.get("/check-email")
def check_email():
    """AJAX endpoint to check for existing email."""
    email = request.args.get("email", "").strip().lower()
    db = SessionLocal()
    exists = db.query(User).filter_by(email=email).first() is not None
    db.close()
    return jsonify({"exists": exists})


@bp.route("/password-reset", methods=["GET", "POST"])
def password_reset_request():
    """Handle password reset email requests."""
    error = None
    message = None
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        db = SessionLocal()
        user = db.query(User).filter_by(email=email).first()
        if not email:
            error = "Email is required"
        elif not user:
            error = "Email not found"
        if error is None:
            token = secrets.token_urlsafe(16)
            db.add(PasswordResetToken(token=token, user_id=user.id))
            db.commit()
            reset_link = url_for("auth.password_reset_token", token=token, _external=True)
            print(f"Password reset link for {email}: {reset_link}")
            message = "If the email exists, a reset link has been sent."
        db.close()
    return render_template("auth/password_reset_request.html", error=error, message=message)


@bp.route("/password-reset/<token>", methods=["GET", "POST"])
def password_reset_token(token: str):
    """Validate reset token and update password."""
    error = None
    db = SessionLocal()
    record = db.query(PasswordResetToken).filter_by(token=token).first()
    if not record:
        db.close()
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
            user = db.get(User, record.user_id)
            user.password_hash = generate_password_hash(password)
            db.delete(record)
            db.commit()
            db.close()
            return redirect(url_for("auth.password_reset_success"))
    db.close()
    return render_template("auth/password_reset_form.html", error=error, token=token)


@bp.get("/password-reset/success")
def password_reset_success():
    """Display success message after password reset."""
    return render_template("auth/password_reset_success.html")
