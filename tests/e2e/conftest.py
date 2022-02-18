import pytest
from fastapi.testclient import TestClient

from config import get_initial_app_settings
from initialization import init_app
from utils import clear_database


@pytest.fixture(name="app_settings")
def app_settings_fixture():
    return get_initial_app_settings()


@pytest.fixture(name="app")
def app_fixture(app_settings):
    return init_app(app_settings)


@pytest.fixture(name="test_client")
async def test_client_fixture(app, app_settings):
    async with clear_database(app):
        client = TestClient(app.app)
        client.base_url += app_settings.API_PREFIX.rstrip("/") + "/"
        yield client
