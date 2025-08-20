from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Tuple

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.ar_model import AutoReg


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


def fit_ar_model(series: pd.Series) -> Tuple[Dict[str, float], pd.Series]:
    """Fit an autoregressive (AR(1)) model to a price series.

    Parameters
    ----------
    series:
        Time series of prices indexed by date.

    Returns
    -------
    Tuple[Dict[str, float], pandas.Series]
        Dictionary of model parameters and a series of in-sample predictions
        aligned with the input series index.
    """

    clean = series.dropna()
    model = AutoReg(clean, lags=1, old_names=False)
    fitted = model.fit()

    params = {key: float(val) for key, val in fitted.params.items()}
    preds = fitted.fittedvalues
    preds.name = "prediction"
    return params, preds


__all__.append("fit_ar_model")

