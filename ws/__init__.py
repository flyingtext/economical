"""WebSocket handlers using Flask-SocketIO."""
from __future__ import annotations

from flask import request
from flask_socketio import SocketIO, emit, join_room

socketio = SocketIO()


def init_app(app):
    """Initialize SocketIO with the given Flask app."""
    socketio.init_app(app, cors_allowed_origins="*")


@socketio.on("connect", namespace="/ws/notifications")
def notifications_connect():
    """Notify clients they are connected to notifications channel."""
    emit("notification", {"message": "connected"})


@socketio.on("connect", namespace="/ws/datasets")
def datasets_connect():
    """Join a room for a specific dataset."""
    dataset_id = request.args.get("dataset_id")
    if dataset_id:
        join_room(dataset_id)
        emit("dataset_update", {"message": f"joined dataset {dataset_id}"})
    else:
        emit("error", {"message": "dataset_id required"})


@socketio.on("connect", namespace="/ws/models")
def models_connect():
    """Join a room for a specific model."""
    model_id = request.args.get("model_id")
    if model_id:
        join_room(model_id)
        emit("model_update", {"message": f"joined model {model_id}"})
    else:
        emit("error", {"message": "model_id required"})


@socketio.on("connect", namespace="/ws/projects")
def projects_connect():
    """Join a room for a specific project."""
    project_id = request.args.get("project_id")
    if project_id:
        join_room(project_id)
        emit("project_update", {"message": f"joined project {project_id}"})
    else:
        emit("error", {"message": "project_id required"})


# Server-side emit helpers -------------------------------------------------

def emit_notification(message: str) -> None:
    """Emit a notification event to all subscribers."""
    socketio.emit("notification", {"message": message}, namespace="/ws/notifications")


def emit_dataset_update(dataset_id: int, payload: dict) -> None:
    """Emit an update for a dataset room."""
    socketio.emit(
        "dataset_update", payload, namespace="/ws/datasets", room=str(dataset_id)
    )


def emit_model_update(model_id: int | str, payload: dict) -> None:
    """Emit an update for a model room."""
    socketio.emit(
        "model_update", payload, namespace="/ws/models", room=str(model_id)
    )


def emit_project_update(project_id: int, payload: dict) -> None:
    """Emit an update for a project room."""
    socketio.emit(
        "project_update", payload, namespace="/ws/projects", room=str(project_id)
    )
