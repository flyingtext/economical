from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd
import requests


def fetch_series(source: str, symbol: str, start: str, end: str) -> pd.DataFrame:
    """Fetch a time series from a remote source.

    Parameters
    ----------
    source: str
        Base URL of the data source.
    symbol: str
        Identifier of the series.
    start: str
        Start date for the requested range in ``YYYY-MM-DD`` format.
    end: str
        End date for the requested range in ``YYYY-MM-DD`` format.

    Returns
    -------
    pandas.DataFrame
        DataFrame indexed by a ``datetime`` column named ``date`` with a
        ``value`` column.
    """
    url = f"{source.rstrip('/')}/{symbol}"
    params = {"start": start, "end": end}
    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()
    data: list[dict[str, Any]] = response.json()
    df = pd.DataFrame(data)
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"])
        df = df.set_index("date")
    return df


def cache_series(series_id: str, df: pd.DataFrame) -> Path:
    """Cache a DataFrame to ``cache/<series_id>.json``.

    Parameters
    ----------
    series_id: str
        Identifier used for the cached file name.
    df: pandas.DataFrame
        DataFrame to cache.

    Returns
    -------
    pathlib.Path
        Path to the cached file.
    """
    cache_dir = Path("cache")
    cache_dir.mkdir(exist_ok=True)
    file_path = cache_dir / f"{series_id}.json"
    df.to_json(file_path, orient="records", date_format="iso")
    return file_path
