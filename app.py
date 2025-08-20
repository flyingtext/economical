from __future__ import annotations

import os
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask

from routes.data import bp as data_bp
from services.data_ingestion import cache_series, fetch_series

app = Flask(__name__)
app.register_blueprint(data_bp)

SOURCE_URL = os.environ.get("SERIES_SOURCE", "https://example.com/api")
SYMBOL = os.environ.get("SERIES_SYMBOL", "demo")
START_DATE = os.environ.get("SERIES_START", "2000-01-01")
END_DATE = os.environ.get("SERIES_END", datetime.utcnow().strftime("%Y-%m-%d"))

scheduler = BackgroundScheduler()


def fetch_and_cache() -> None:
    df = fetch_series(SOURCE_URL, SYMBOL, START_DATE, END_DATE)
    cache_series(SYMBOL, df)


scheduler.add_job(fetch_and_cache, "cron", hour=0, minute=0)
scheduler.start()


@app.route("/")
def index() -> str:
    return "Service is running"


if __name__ == "__main__":
    app.run()
