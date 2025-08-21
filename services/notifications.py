"""Notification service backed by the database."""
from __future__ import annotations

from typing import Dict, Any

from models import Notification
from models.db import SessionLocal
from ws import emit_user_notification


def _to_payload(notification: Notification) -> Dict[str, Any]:
    """Serialize a ``Notification`` instance for websocket emission."""

    return {
        "id": notification.id,
        "message": notification.message,
        "type": notification.type,
        "is_read": notification.is_read,
        "created_at": notification.created_at.isoformat(),
    }


def create_notification(user: str, message: str, type: str) -> Notification:
    """Create a notification for ``user`` and push it to active sessions."""

    with SessionLocal() as session:
        notification = Notification(user_id=user, message=message, type=type)
        session.add(notification)
        session.commit()
        session.refresh(notification)

    emit_user_notification(user, _to_payload(notification))
    return notification


def update_notification(notification_id: str, **changes) -> Notification:
    """Update an existing notification and push changes to the user."""

    with SessionLocal() as session:
        notification = session.get(Notification, notification_id)
        for key, value in changes.items():
            setattr(notification, key, value)
        session.commit()
        session.refresh(notification)
        user = notification.user_id

    emit_user_notification(user, _to_payload(notification))
    return notification
