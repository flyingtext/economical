from __future__ import annotations

"""Category metadata for the application.

This module defines static category information that can be imported from
routes and templates without executing any I/O on import.
"""

from flask import Blueprint, render_template
from typing import Dict, List, TypedDict


class Category(TypedDict):
    """Structure describing a single category."""

    name: str
    description: str
    deterministic_examples: List[str]
    stochastic_examples: List[str]
    adaptability: str
    related_categories: List[str]
    links: Dict[str, str]


CATEGORIES: Dict[str, Category] = {
    "economics": {
        "name": "Economics",
        "description": "Models and indicators related to economic trends.",
        "deterministic_examples": ["GDP growth", "inflation rate"],
        "stochastic_examples": ["market volatility", "interest rate shocks"],
        "adaptability": "High",
        "related_categories": ["finance", "statistics"],
        "links": {
            "GDP growth": "/categories/finance#stock-price-simulation",
        },
    },
    "finance": {
        "name": "Finance",
        "description": "Financial modelling techniques for assets and risk.",
        "deterministic_examples": ["bond pricing", "option payoff"],
        "stochastic_examples": ["stock price simulation", "risk models"],
        "adaptability": "Medium",
        "related_categories": ["economics"],
        "links": {
            "stock price simulation": "/categories/economics#gdp-growth",
        },
    },
    "statistics": {
        "name": "Statistics",
        "description": "Statistical tools and models.",
        "deterministic_examples": ["mean", "variance"],
        "stochastic_examples": ["monte carlo", "bootstrap"],
        "adaptability": "High",
        "related_categories": ["economics", "finance"],
        "links": {},
    },
    "machine_learning": {
        "name": "Machine Learning",
        "description": "Learning algorithms for prediction and classification.",
        "deterministic_examples": ["linear regression", "decision tree"],
        "stochastic_examples": ["random forest", "neural network"],
        "adaptability": "Medium",
        "related_categories": ["statistics"],
        "links": {},
    },
    "data_science": {
        "name": "Data Science",
        "description": "Data processing and visualization techniques.",
        "deterministic_examples": ["ETL process", "data cleaning"],
        "stochastic_examples": ["data sampling", "randomization"],
        "adaptability": "Low",
        "related_categories": ["machine_learning"],
        "links": {},
    },
}


def get_categories() -> List[Category]:
    """Return all category definitions."""

    return list(CATEGORIES.values())


bp = Blueprint("categories", __name__, url_prefix="/categories")


@bp.get("/")
def index() -> str:
    """Render the categories page."""

    return render_template("categories.html", categories=get_categories())


@bp.get("/<path:subpath>")
def anchor(subpath: str) -> str:
    """Allow category path segments for anchor links."""

    return index()
