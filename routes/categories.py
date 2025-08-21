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
        "description": "General statistical tools used across domains.",
        "deterministic_examples": ["linear regression", "hypothesis testing"],
        "stochastic_examples": ["monte carlo methods", "bootstrap"],
        "adaptability": "High",
        "related_categories": ["economics", "machine-learning"],
        "links": {},
    },
    "machine-learning": {
        "name": "Machine Learning",
        "description": "Data-driven algorithms for pattern finding and prediction.",
        "deterministic_examples": ["decision tree", "support vector machine"],
        "stochastic_examples": ["random forest", "neural network"],
        "adaptability": "High",
        "related_categories": ["statistics", "optimization"],
        "links": {},
    },
    "optimization": {
        "name": "Optimization",
        "description": "Approaches for selecting best outcomes under constraints.",
        "deterministic_examples": ["linear programming", "gradient descent"],
        "stochastic_examples": ["simulated annealing", "genetic algorithms"],
        "adaptability": "Low",
        "related_categories": ["machine-learning"],
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
