from pathlib import Path

import pytest
from fastapi.testclient import TestClient
from fastapi_ecommerce.models.base import Base, _engine, db_settings

from main import app


@pytest.fixture(scope="session")
def test_app_with_db():

    Base.metadata.create_all(bind=_engine)

    with TestClient(app) as test_client:
        yield test_client

    Base.metadata.drop_all(bind=_engine)
    
    if _engine.url.drivername == "sqlite":
        file_path = Path(_engine.url.database)
        file_path.unlink()
