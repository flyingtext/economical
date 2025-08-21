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

from werkzeug.security import generate_password_hash
from models.db import SessionLocal
from models.user import User, ActiveSession

bp = Blueprint("my_account", __name__, url_prefix="/my-account")


def _current_user_id() -> int | None:
    return session.get("user_id")


@bp.before_request
def require_login() -> Any:
    if "user_id" not in session:
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
    user_id = _current_user_id()
    if user_id is None:
        return redirect(url_for("auth.login"))
    db = SessionLocal()
    user = db.get(User, user_id)
    action = request.form.get("action")
    if request.method == "POST" and action:
        if action == "update_profile":
            user.name = request.form.get("name", user.name)
            user.affiliation = request.form.get("affiliation", getattr(user, "affiliation", ""))
            orcid = request.form.get("orcid", "").strip() or None
            setattr(user, "orcid", orcid)
        elif action == "change_password":
            new_pwd = request.form.get("password")
            if new_pwd:
                user.password_hash = generate_password_hash(new_pwd)
        db.commit()
    sessions = db.query(ActiveSession).filter_by(user_id=user.id).all()
    orcid_name = _fetch_orcid_name(getattr(user, "orcid", "")) if getattr(user, "orcid", None) else None
    resp = render_template(
        "my_account/index.html",
        user=user,
        sessions=sessions,
        orcid_name=orcid_name,
    )
    db.close()
    return resp


@bp.post("/session/<token>/revoke")
def revoke_session(token: str):
    user_id = _current_user_id()
    if user_id is None:
        return redirect(url_for("auth.login"))
    db = SessionLocal()
    sess = db.query(ActiveSession).filter_by(user_id=user_id, token=token).first()
    if sess:
        db.delete(sess)
        db.commit()
    db.close()
    if session.get("session_token") == token:
        session.clear()
        return redirect(url_for("auth.login"))
    return redirect(url_for("my_account.dashboard"))
