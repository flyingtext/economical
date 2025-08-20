from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd
import requests
import yfinance as yf


def fetch_series(ticker: str, start: str, end: str | None = None) -> pd.DataFrame:
    """Retrieve a price series from Yahoo Finance.

    Parameters
    ----------
    ticker:
        Ticker symbol understood by Yahoo Finance.
    start:
        Start date in ``YYYY-MM-DD`` format.
    end:
        End date in ``YYYY-MM-DD`` format. If ``None`` the latest available
        date is used.

    Returns
    -------
    pandas.DataFrame
        DataFrame indexed by ``date`` with a ``value`` column containing the
        adjusted close prices.
    """

    data = yf.download(ticker, start=start, end=end, progress=False)
    if data.empty:
        return pd.DataFrame(columns=["value"])
    price_col = "Adj Close" if "Adj Close" in data.columns else "Close"
    df = data[[price_col]].rename(columns={price_col: "value"})
    df.index.name = "date"
    return df


def fetch_remote_series(source: str, symbol: str, start: str, end: str) -> pd.DataFrame:
    """Fetch a time series from a generic remote JSON source."""

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


def fetch_market_data(symbol: str, start: str, end: str | None = None) -> pd.DataFrame:
    """Fetch market data using the Yahoo Finance API.

    Parameters
    ----------
    symbol: str
        Ticker symbol understood by Yahoo Finance.
    start: str
        Start date in ``YYYY-MM-DD`` format.
    end: str
        End date in ``YYYY-MM-DD`` format.

    Returns
    -------
    pandas.DataFrame
        DataFrame with a ``value`` column containing the adjusted close
        prices indexed by date.
    """

    data = yf.download(symbol, start=start, end=end, progress=False)
    if data.empty:
        return pd.DataFrame(columns=["value"])
    price_col = "Adj Close" if "Adj Close" in data.columns else "Close"
    df = data[[price_col]].rename(columns={price_col: "value"})
    df.index.name = "date"
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


def build_features(series: pd.Series, options: list[str]) -> pd.DataFrame:
    """Compute derived indicators for a price series.

    Parameters
    ----------
    series:
        Raw price series.
    options:
        List of indicator names to compute. Supported values are
        ``"moving_average"`` and ``"return"``.

    Returns
    -------
    pandas.DataFrame
        DataFrame containing the original ``value`` column along with any
        requested indicators.
    """

    df = pd.DataFrame({"value": series})
    if "moving_average" in options:
        df["moving_average"] = series.rolling(window=5).mean()
    if "return" in options:
        df["return"] = series.pct_change()
    return df.dropna()
