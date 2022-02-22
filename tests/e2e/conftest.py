from typing import Dict, List

import pytest
from config import get_initial_app_settings
from domain.entities import AbstractEntity
from fastapi.testclient import TestClient
from initialization import init_app
from utils import clear_database


@pytest.fixture(name="app_settings")
def app_settings_fixture():
    return get_initial_app_settings()


@pytest.fixture(name="app")
def app_fixture(app_settings):
    return init_app(app_settings)


@pytest.fixture(name="test_client")
def test_client_fixture(app, app_settings):
    with clear_database(app):
        client = TestClient(app.app)
        client.base_url += app_settings.API_PREFIX.rstrip("/") + "/"
        yield client


@pytest.fixture(name="test_client_and_data")
def test_client_and_data_fixture(app, app_settings, fill_database):
    with clear_database(app):
        app.db = fill_database(app.db)
        client = TestClient(app.app)
        client.base_url += app_settings.API_PREFIX.rstrip("/") + "/"
        yield client, None if not app.db.repositories else list(
            app.db.repositories.values()
        )[0].session.data


@pytest.fixture(name="test_data")
def test_data_fixture(test_client_and_data) -> Dict[str, List[AbstractEntity]]:
    _, data = test_client_and_data
    return data
