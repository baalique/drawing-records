import pytest
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.config import get_initial_app_settings
from app.infrastructure.adapters.orm import metadata


@pytest.fixture(name="postgresql_engine")
async def postgresql_engine_fixture():
    engine = create_async_engine(get_initial_app_settings().test_dsn)
    metadata.bind = engine
    async with engine.begin() as conn:
        await conn.run_sync(metadata.drop_all)
        await conn.run_sync(metadata.create_all)
    return engine


@pytest.fixture(name="session_factory")
def session_factory_fixture(postgresql_engine):
    return sessionmaker(
        bind=postgresql_engine,
        class_=AsyncSession,
        autocommit=False,
        autoflush=False,
        expire_on_commit=False,
    )
