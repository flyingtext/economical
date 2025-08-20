from __future__ import annotations

import base64
import io

from flask import Blueprint, render_template, request

import matplotlib.pyplot as plt

from services.data_ingestion import fetch_series
from services.modeling import fit_ar_model

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

    df = fetch_series(symbol, start, end or None)
    params, preds = fit_ar_model(df["value"])

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

    return render_template(
        "model_result.html",
        symbol=symbol,
        params=params,
        plot_data=plot_data,
    )

