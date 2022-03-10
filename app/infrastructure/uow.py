from types import TracebackType
from typing import AsyncGenerator, Callable, Type

from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.adapters.repositories.drawing import SQLAlchemyDrawingRepository
from app.infrastructure.protocols import UnitOfWork


class SQLAlchemyUnitOfWork(UnitOfWork):
    def __init__(
        self, session_factory: Callable[[], AsyncGenerator[AsyncSession, None]]
    ):
        self.session_factory = session_factory

    def __call__(self) -> "SQLAlchemyUnitOfWork":
        return self

    async def __aenter__(self) -> "SQLAlchemyUnitOfWork":
        self.session = await anext(self.session_factory())
        self.drawings = SQLAlchemyDrawingRepository(self.session)
        return self

    async def __aexit__(
        self, exc_type: Type[Exception], exc: Exception, tb: TracebackType
    ) -> None:
        await self.rollback()
        await self.session.close()

    async def commit(self) -> None:
        await self.session.commit()

    async def rollback(self) -> None:
        await self.session.rollback()
