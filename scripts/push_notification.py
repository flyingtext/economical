"""Utility script to simulate server push during development."""

from __future__ import annotations

import sys

from app import app
from services.notifications import create_notification


def main() -> None:
    user = sys.argv[1] if len(sys.argv) > 1 else "test@example.com"
    message = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else "Hello from dev script"
    with app.app_context():
        create_notification(user, message, "info")


if __name__ == "__main__":
    main()

