import os
import tempfile

import pytest

from app import create_app
from app.models import db


@pytest.fixture
def client():
    db_fd, db_path = tempfile.mkstemp()
    app = create_app(
        {
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": f"sqlite:///{db_path}",
        }
    )

    with app.app_context():
        db.create_all()

    with app.test_client() as client:
        yield client

    os.close(db_fd)
    os.unlink(db_path)

