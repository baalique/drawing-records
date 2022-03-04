from typing import Dict, List

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import create_async_engine

from app.config import get_initial_app_settings
from app.infrastructure.adapters.orm import metadata
from app.infrastructure.db.db import get_db
from app.initialization import init_app
from app.service_layer.dtos import AbstractDtoOut
from tests.utils import clear_database, get_test_db


@pytest.fixture(name="app_settings")
def app_settings_fixture():
    return get_initial_app_settings()


@pytest.fixture(name="app")
def app_fixture(app_settings):
    return init_app(app_settings)


@pytest.fixture(name="recreate_db")
async def _recreate_db_fixture():
    engine = create_async_engine(
        get_initial_app_settings().test_dsn, pool_pre_ping=True
    )
    metadata.bind = engine
    async with engine.begin() as conn:
        await conn.run_sync(metadata.drop_all)
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)


@pytest.fixture(name="test_client")
def test_client_fixture(app, app_settings, recreate_db):
    app.app.dependency_overrides[get_db] = get_test_db
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
def test_data_fixture(test_client_and_data) -> Dict[str, List[AbstractDtoOut]]:
    _, data = test_client_and_data
    return data
