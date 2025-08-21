"""Authentication and account related routes."""

from flask import (
    Blueprint,
    render_template,
    redirect,
    request,
    url_for,
    jsonify,
)

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/login", methods=["GET", "POST"])
def login():
    """Render the login page and handle basic login submissions."""
    error = None
    if request.method == "POST":
        email = request.form.get("email", "")
        password = request.form.get("password", "")
        # Placeholder authentication logic. Accept any non-empty credentials.
        if email and password:
            return redirect(url_for("index"))
        error = "Invalid credentials"
        if request.headers.get("X-Requested-With") == "XMLHttpRequest":
            return jsonify({"error": error}), 400
    return render_template("auth/login.html", error=error)


@bp.get("/signup")
def signup():
    """Render the sign up page."""
    return render_template("auth/signup.html")


@bp.get("/password-reset")
def password_reset():
    """Render the password reset page."""
    return render_template("auth/password_reset.html")
