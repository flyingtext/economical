from __future__ import annotations

"""Category metadata for the application.

This module defines static category information that can be imported from
routes and templates without executing any I/O on import.
"""

from typing import Dict, List, TypedDict


class Category(TypedDict):
    """Structure describing a single category."""

    name: str
    description: str
    deterministic_examples: List[str]
    stochastic_examples: List[str]
    adaptability: str
    related_categories: List[str]


CATEGORIES: Dict[str, Category] = {
    "economics": {
        "name": "Economics",
        "description": "Models and indicators related to economic trends.",
        "deterministic_examples": ["GDP growth", "inflation rate"],
        "stochastic_examples": ["market volatility", "interest rate shocks"],
        "adaptability": "High",
        "related_categories": ["finance", "statistics"],
    },
    "finance": {
        "name": "Finance",
        "description": "Financial modelling techniques for assets and risk.",
        "deterministic_examples": ["bond pricing", "option payoff"],
        "stochastic_examples": ["stock price simulation", "risk models"],
        "adaptability": "Medium",
        "related_categories": ["economics"],
    },
}


def get_categories() -> List[Category]:
    """Return all category definitions."""

    return list(CATEGORIES.values())
