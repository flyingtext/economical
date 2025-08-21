import importlib.util
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from routes.auth import registered_users, reset_tokens  # type: ignore  # noqa: E402


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


def setup_function():
    registered_users.clear()
    reset_tokens.clear()


def test_password_reset_flow(client):
    registered_users.append({'name': 'Test', 'email': 'test@example.com', 'password': 'OldPass123', 'contact': ''})
    resp = client.post('/auth/password-reset', data={'email': 'test@example.com'})
    assert resp.status_code == 200
    assert b'reset link' in resp.data.lower()
    assert reset_tokens
    token = next(iter(reset_tokens))
    resp = client.post(f'/auth/password-reset/{token}', data={'password': 'NewPass123', 'confirm': 'NewPass123'}, follow_redirects=True)
    assert resp.status_code == 200
    assert b'Password Reset Successful' in resp.data
    assert registered_users[0]['password'] == 'NewPass123'
