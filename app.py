from __future__ import annotations

import os
from flask import Flask, g, abort, render_template
from dotenv import load_dotenv

load_dotenv()

from routes.data import bp as data_bp
from routes.model import bp as model_bp
from routes.categories import bp as categories_bp
from routes.auth import bp as auth_bp
from routes.my_account import bp as my_account_bp
from routes.datasets import bp as datasets_bp
from routes.projects import bp as projects_bp
from routes.dashboards import bp as dashboards_bp
from routes.community import bp as community_bp
from routes.notifications import bp as notifications_bp
from routes.admin import bp as admin_bp
from routes.api_datasets import bp as api_datasets_bp
from routes.api_projects import bp as api_projects_bp
from routes.api_dashboards import bp as api_dashboards_bp
from ws import init_app as init_ws, socketio
from models.db import Base, engine, SessionLocal

# Ensure tables exist
Base.metadata.create_all(bind=engine)

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev")
app.register_blueprint(data_bp)
app.register_blueprint(model_bp)
app.register_blueprint(categories_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(my_account_bp)
app.register_blueprint(datasets_bp)
app.register_blueprint(projects_bp)
app.register_blueprint(dashboards_bp)
app.register_blueprint(community_bp)
app.register_blueprint(notifications_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(api_datasets_bp)
app.register_blueprint(api_projects_bp)
app.register_blueprint(api_dashboards_bp)

init_ws(app)


def get_session():
    """Return a scoped SQLAlchemy session for the current request."""

    if "db" not in g:
        g.db = SessionLocal()
    return g.db


@app.teardown_appcontext
def remove_session(exc=None):
    """Close the database session at the end of the request."""

    session = g.pop("db", None)
    if session is not None:
        session.close()


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def index(path: str) -> str:
    if path.startswith("api") or path.startswith("ws"):
        abort(404)
    return render_template("index.html")


if __name__ == "__main__":
    host = os.environ.get("HOST", "127.0.0.1")
    port = int(os.environ.get("PORT", 5000))
    socketio.run(app, host=host, port=port)
