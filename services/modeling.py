from __future__ import annotations

from dataclasses import dataclass
from typing import Dict

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


@dataclass
class ModelResult:
    """Container for fitted model parameters and validation metric."""

    coef: float
    intercept: float
    rmse: float


def _prepare_features(df: pd.DataFrame) -> pd.DataFrame:
    """Convert raw price series into modelling features.

    Parameters
    ----------
    df:
        DataFrame with a ``value`` column representing the price series.

    Returns
    -------
    pandas.DataFrame
        DataFrame with percentage returns and a one day lag feature.
    """

    data = df.copy()
    data["return"] = data["value"].pct_change()
    data["lag1"] = data["return"].shift(1)
    data = data.dropna()
    return data


def fit_and_validate(df: pd.DataFrame, holdout: int = 5) -> ModelResult:
    """Fit a simple autoregressive model and validate on a holdout set.

    The function uses the previous day's return to predict the next day's
    return via linear regression. The last ``holdout`` observations are used
    for validation and the root mean squared error (RMSE) is reported.
    """

    features = _prepare_features(df)
    if len(features) <= holdout:
        raise ValueError("Not enough data for the requested holdout size")

    train = features.iloc[:-holdout]
    test = features.iloc[-holdout:]

    model = LinearRegression()
    model.fit(train[["lag1"]], train["return"])

    preds = model.predict(test[["lag1"]])
    rmse = float(mean_squared_error(test["return"], preds, squared=False))

    return ModelResult(
        coef=float(model.coef_[0]),
        intercept=float(model.intercept_),
        rmse=rmse,
    )


__all__ = ["fit_and_validate", "ModelResult"]

