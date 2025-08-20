from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, Tuple

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.ar_model import AutoReg
from statsmodels.tsa.api import VAR


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


# ---------------------------------------------------------------------------
# Object oriented models


class BaseModel(ABC):
    """Abstract base class for time series models."""

    @abstractmethod
    def fit(self, data: pd.Series | pd.DataFrame) -> "BaseModel":
        """Fit the model to the provided data."""

    @abstractmethod
    def predict(self, steps: int | None = None) -> pd.Series | pd.DataFrame:
        """Generate in-sample predictions or out-of-sample forecasts."""

    @property
    @abstractmethod
    def params(self) -> Dict[str, float]:
        """Return model parameters as a dictionary."""


class ARModel(BaseModel):
    """Autoregressive model wrapper using ``statsmodels`` AutoReg."""

    def __init__(self, lags: int = 1) -> None:
        self.lags = lags
        self._result = None

    def fit(self, data: pd.Series) -> "ARModel":
        clean = data.dropna()
        model = AutoReg(clean, lags=self.lags, old_names=False)
        self._result = model.fit()
        return self

    def predict(self, steps: int | None = None) -> pd.Series:
        if self._result is None:
            raise RuntimeError("Model must be fit before prediction")
        preds = self._result.fittedvalues
        if steps:
            forecast = self._result.predict(
                start=len(preds), end=len(preds) + steps - 1
            )
            preds = pd.concat([preds, forecast])
        preds.name = "prediction"
        return preds

    @property
    def params(self) -> Dict[str, float]:
        if self._result is None:
            return {}
        return {k: float(v) for k, v in self._result.params.items()}


class VARModel(BaseModel):
    """Vector autoregression model using ``statsmodels`` VAR."""

    def __init__(self, lags: int = 1) -> None:
        self.lags = lags
        self._result = None
        self._index = None

    def fit(self, data: pd.DataFrame) -> "VARModel":
        clean = data.dropna()
        model = VAR(clean)
        self._result = model.fit(self.lags)
        # fitted values start after ``k_ar`` observations
        self._index = clean.index[self._result.k_ar :]
        return self

    def predict(self, steps: int | None = None) -> pd.DataFrame:
        if self._result is None:
            raise RuntimeError("Model must be fit before prediction")
        preds = self._result.fittedvalues
        preds.index = self._index
        if steps:
            forecast = self._result.forecast(self._result.y, steps)
            forecast_index = pd.RangeIndex(len(self._index), len(self._index) + steps)
            forecast_df = pd.DataFrame(forecast, columns=preds.columns, index=forecast_index)
            preds = pd.concat([preds, forecast_df])
        return preds

    @property
    def params(self) -> Dict[str, float]:
        if self._result is None:
            return {}
        return {k: float(v) for k, v in self._result.params.items()}


__all__ = [
    "fit_and_validate",
    "ModelResult",
    "fit_ar_model",
    "BaseModel",
    "ARModel",
    "VARModel",
]

