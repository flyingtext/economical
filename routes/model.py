from __future__ import annotations

from flask import Blueprint, render_template, request

from services.data_ingestion import fetch_market_data
from services.modeling import fit_and_validate

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

    df = fetch_market_data(symbol, start, end or None)
    result = fit_and_validate(df)

    return render_template("model.html", result=result, symbol=symbol)

