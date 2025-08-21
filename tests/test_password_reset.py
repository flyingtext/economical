import os
import sys
from pathlib import Path
import importlib.util

import pytest
from werkzeug.security import generate_password_hash, check_password_hash

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

os.environ["DATABASE_URL"] = "sqlite:///:memory:"

from models.db import Base, engine, SessionLocal  # type: ignore  # noqa: E402
from models.user import User, PasswordResetToken  # type: ignore  # noqa: E402


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
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


def test_password_reset_flow(client):
    db = SessionLocal()
    db.add(User(name='Test', email='test@example.com', password_hash=generate_password_hash('OldPass123')))
    db.commit()
    db.close()
    resp = client.post('/auth/password-reset', data={'email': 'test@example.com'})
    assert resp.status_code == 200
    assert b'reset link' in resp.data.lower()
    db = SessionLocal()
    token_obj = db.query(PasswordResetToken).first()
    assert token_obj is not None
    token = token_obj.token
    user_id = token_obj.user_id
    db.close()
    resp = client.post(f'/auth/password-reset/{token}', data={'password': 'NewPass123', 'confirm': 'NewPass123'}, follow_redirects=True)
    assert resp.status_code == 200
    assert b'Password Reset Successful' in resp.data
    db = SessionLocal()
    user = db.get(User, user_id)
    assert user is not None and check_password_hash(user.password_hash, 'NewPass123')
    db.close()
