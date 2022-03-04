from contextlib import contextmanager
from typing import Any, Callable, List, Optional

from factory.base import FactoryMetaClass
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.application import Application
from app.config import get_initial_app_settings
from app.infrastructure.adapters.orm import metadata


def make_many(
    factory: FactoryMetaClass,
    amount: int,
    primary_key_expression: Optional[Callable[[FactoryMetaClass], Any]] = None,
) -> List[Any]:
    if not primary_key_expression:
        return [factory() for _ in range(amount)]

    objs = []
    _pks = {}
    c = 0
    while True:
        if c >= amount:
            return objs
        obj = factory()
        if primary_key_expression(obj) not in _pks:
            objs.append(obj)
            c += 1


@contextmanager
def clear_database(app: Application):
    yield


async def _init_test_db(dsn: str) -> sessionmaker:
    engine = create_async_engine(dsn, pool_pre_ping=True)
    metadata.bind = engine
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)
    return sessionmaker(
        bind=engine,
        class_=AsyncSession,
        autocommit=False,
        autoflush=False,
        expire_on_commit=False,
    )


async def get_test_db() -> AsyncSession:
    session_factory = await _init_test_db(get_initial_app_settings().test_dsn)
    async with session_factory() as session:
        yield session
