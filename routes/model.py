from __future__ import annotations

import base64
import io

from flask import Blueprint, render_template, request, url_for
from ws import emit_model_update

import matplotlib.pyplot as plt

from services.data_ingestion import build_features, fetch_series
from services.modeling import ARModel, VARModel

bp = Blueprint("model", __name__, url_prefix="/model")


@bp.get("/")
def form() -> str:
    """Render a simple form for model fitting."""

    return render_template("model.html")


@bp.post("/")
def run_model() -> str:
    """Execute the modelling pipeline and display results."""

    symbol = request.form.get("symbol", "")
    start = request.form.get("start", "2000-01-01")
    end = request.form.get("end", "")
    model_type = request.form.get("model_type", "ar")
    indicator_opts = request.form.getlist("indicators")

    category_map = {"ar": "time-series", "var": "time-series"}
    category_slug = category_map.get(model_type)
    category_url = (
        url_for("categories.anchor", subpath=category_slug)
        if category_slug
        else url_for("categories.index")
    )

    df = fetch_series(symbol, start, end or None)
    features = build_features(df["value"], indicator_opts)

    if model_type == "var" and features.shape[1] > 1:
        model = VARModel()
        model.fit(features)
        preds = model.predict()["value"]
    else:
        model = ARModel()
        model.fit(df["value"])
        preds = model.predict()

    fig, ax = plt.subplots()
    df["value"].plot(ax=ax, label="Actual")
    preds.plot(ax=ax, label="Predicted")
    ax.legend()
    ax.set_title(symbol)

    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    plot_data = base64.b64encode(buf.getvalue()).decode("ascii")
    plt.close(fig)

    latest_indicators = (
        features.drop(columns=["value"]).iloc[-1].to_dict()
        if not features.empty
        else {}
    )
    
    emit_model_update(model_type, {"message": f"model run for {symbol}"})
    return render_template(
        "model_result.html",
        symbol=symbol,
        params=model.params,
        indicators=latest_indicators,
        plot_data=plot_data,
        category_url=category_url,
    )

