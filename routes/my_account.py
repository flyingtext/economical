"""My Account dashboard and settings routes."""

from __future__ import annotations

from datetime import datetime
from typing import Any

import requests
from flask import (
    Blueprint,
    render_template,
    session,
    redirect,
    url_for,
    request,
)

from .auth import registered_users, active_sessions

bp = Blueprint("my_account", __name__, url_prefix="/my-account")


def _current_user() -> dict | None:
    email = session.get("user")
    if not email:
        return None
    for user in registered_users:
        if user.get("email") == email:
            return user
    return None


@bp.before_request
def require_login() -> Any:
    if "user" not in session:
        return redirect(url_for("auth.login"))
    return None


def _fetch_orcid_name(orcid_id: str) -> str | None:
    try:
        resp = requests.get(
            f"https://pub.orcid.org/v3.0/{orcid_id}",
            headers={"Accept": "application/json"},
            timeout=5,
        )
        if resp.ok:
            data = resp.json()
            name = data.get("person", {}).get("name", {})
            given = name.get("given-names", {}).get("value", "")
            family = name.get("family-name", {}).get("value", "")
            return f"{given} {family}".strip() or None
    except Exception:
        pass
    return None


@bp.route("/", methods=["GET", "POST"])
@bp.route("", methods=["GET", "POST"])
def dashboard():
    user = _current_user()
    if user is None:
        return redirect(url_for("auth.login"))
    action = request.form.get("action")
    if request.method == "POST" and action:
        if action == "update_profile":
            user["name"] = request.form.get("name", user.get("name"))
            user["affiliation"] = request.form.get(
                "affiliation", user.get("affiliation", "")
            )
            orcid = request.form.get("orcid", "").strip() or None
            user["orcid"] = orcid
        elif action == "change_password":
            new_pwd = request.form.get("password")
            if new_pwd:
                user["password"] = new_pwd
        elif action == "update_preferences":
            prefs = user.setdefault("preferences", {})
            prefs["language"] = request.form.get("language", prefs.get("language"))
            prefs["timezone"] = request.form.get("timezone", prefs.get("timezone"))
            prefs["theme"] = request.form.get("theme", prefs.get("theme"))
            notes = user.setdefault("notifications", {})
            notes["email"] = bool(request.form.get("notify_email"))
            notes["in_app"] = bool(request.form.get("notify_in_app"))
        elif action == "request_backup":
            user.setdefault("backups", []).append(
                {
                    "requested_at": datetime.utcnow(),
                    "status": "Processing",
                }
            )
    sessions = active_sessions.get(user["email"], [])
    orcid_name = _fetch_orcid_name(user.get("orcid")) if user.get("orcid") else None
    return render_template(
        "my_account/index.html",
        user=user,
        sessions=sessions,
        orcid_name=orcid_name,
    )


@bp.post("/session/<token>/revoke")
def revoke_session(token: str):
    user = _current_user()
    if user is None:
        return redirect(url_for("auth.login"))
    user_sessions = active_sessions.get(user["email"], [])
    active_sessions[user["email"]] = [s for s in user_sessions if s["token"] != token]
    if session.get("session_token") == token:
        session.clear()
        return redirect(url_for("auth.login"))
    return redirect(url_for("my_account.dashboard"))
