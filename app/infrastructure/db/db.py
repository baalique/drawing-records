from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.config import get_current_app_settings
from app.infrastructure.adapters.orm import start_mappers


def init_db() -> sessionmaker:
    settings = get_current_app_settings()

    engine = create_async_engine(settings.dsn, pool_pre_ping=True)
    start_mappers()

    return sessionmaker(
        bind=engine,
        class_=AsyncSession,
        autocommit=False,
        autoflush=False,
        expire_on_commit=False,
    )


session_factory = init_db()


async def get_db() -> AsyncGenerator:
    async with session_factory() as session:
        yield session
