from __future__ import annotations

import os
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
from dotenv import load_dotenv

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
from services.data_ingestion import cache_series, fetch_remote_series
from ws import init_app as init_ws, socketio
from models.db import Base, engine

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

init_ws(app)

load_dotenv()

SOURCE_URL = os.environ.get("SERIES_SOURCE", "https://example.com/api")
SYMBOL = os.environ.get("SERIES_SYMBOL", "demo")
START_DATE = os.environ.get("SERIES_START", "2000-01-01")
END_DATE = os.environ.get("SERIES_END", datetime.utcnow().strftime("%Y-%m-%d"))

scheduler = BackgroundScheduler()


def fetch_and_cache() -> None:
    df = fetch_remote_series(SOURCE_URL, SYMBOL, START_DATE, END_DATE)
    cache_series(SYMBOL, df)


scheduler.add_job(fetch_and_cache, "cron", hour=0, minute=0)
scheduler.start()


@app.route("/")
def index() -> str:
    return "Service is running"


if __name__ == "__main__":
    socketio.run(app)
