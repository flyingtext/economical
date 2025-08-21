"""In-memory notification service with WebSocket push support."""
from __future__ import annotations

from dataclasses import asdict
from itertools import count
from typing import Dict, Tuple

from models import Notification
from ws import emit_user_notification

# Simple in-memory store for notifications {id: (user_email, Notification)}
_notifications: Dict[int, Tuple[str, Notification]] = {}
_ids = count(1)


def create_notification(user: str, message: str, type: str) -> Notification:
    """Create a notification for ``user`` and push it to active sessions."""
    notification = Notification(id=next(_ids), message=message, type=type)
    _notifications[notification.id] = (user, notification)
    payload = asdict(notification)
    payload["created_at"] = notification.created_at.isoformat()
    emit_user_notification(user, payload)
    return notification


def update_notification(notification_id: int, **changes) -> Notification:
    """Update an existing notification and push changes to the user."""
    user, notification = _notifications[notification_id]
    for key, value in changes.items():
        setattr(notification, key, value)
    payload = asdict(notification)
    payload["created_at"] = notification.created_at.isoformat()
    emit_user_notification(user, payload)
    return notification

