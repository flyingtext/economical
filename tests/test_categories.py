import importlib.util
import sys
from pathlib import Path

import pytest

# Ensure project root is on sys.path for module imports
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from routes.categories import get_categories  # type: ignore  # noqa: E402


def _load_flask_app():
    app_path = ROOT / 'app.py'
    spec = importlib.util.spec_from_file_location('app_main', app_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)  # type: ignore[attr-defined]
    return module.app


@pytest.fixture
def client():
    app = _load_flask_app()
    return app.test_client()


def test_categories_endpoint(client):
    """Ensure the /categories page renders successfully and shows category names."""
    response = client.get('/categories/')
    assert response.status_code == 200
    html = response.data.decode('utf-8')
    for category in get_categories():
        assert category['name'] in html


def test_get_categories_returns_all_five_with_fields():
    """Verify get_categories returns five categories with required fields."""
    categories = get_categories()
    assert len(categories) == 5
    required_fields = {
        'name',
        'description',
        'deterministic_examples',
        'stochastic_examples',
        'adaptability',
        'related_categories',
        'links',
    }
    for cat in categories:
        assert required_fields.issubset(cat)
