from __future__ import annotations

import os
from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
from dotenv import load_dotenv

from services.data_ingestion import cache_series, fetch_remote_series

load_dotenv()

SOURCE_URL = os.environ.get("SERIES_SOURCE", "https://example.com/api")
SYMBOL = os.environ.get("SERIES_SYMBOL", "demo")
START_DATE = os.environ.get("SERIES_START", "2000-01-01")
END_DATE = os.environ.get("SERIES_END", datetime.utcnow().strftime("%Y-%m-%d"))


def fetch_and_cache() -> None:
    df = fetch_remote_series(SOURCE_URL, SYMBOL, START_DATE, END_DATE)
    cache_series(SYMBOL, df)


if __name__ == "__main__":
    scheduler = BlockingScheduler()
    scheduler.add_job(fetch_and_cache, "cron", hour=0, minute=0)
    scheduler.start()
