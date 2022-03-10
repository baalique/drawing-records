from __future__ import annotations

from types import TracebackType
from typing import Type

from app.infrastructure.adapters.repositories.protocols import WriteableRepository


class UnitOfWork:
    drawings: WriteableRepository

    def __call__(self):
        ...

    async def __aenter__(self) -> UnitOfWork:
        ...

    async def __aexit__(
        self, exc_type: Type[Exception], exc: Exception, tb: TracebackType
    ) -> None:
        ...

    async def commit(self) -> None:
        ...

    async def rollback(self) -> None:
        ...
