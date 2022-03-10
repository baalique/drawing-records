from typing import AsyncGenerator, Callable

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker


def get_session_factory(
    dsn: str, echo: bool
) -> Callable[[], AsyncGenerator[AsyncSession, None]]:
    engine = create_async_engine(dsn, echo=echo)

    session = sessionmaker(
        bind=engine,
        class_=AsyncSession,
        autocommit=False,
        autoflush=False,
        expire_on_commit=False,
    )

    async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
        db = session()
        try:
            yield db
        finally:
            db.close()

    return get_db_session
