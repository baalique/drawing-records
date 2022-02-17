from __future__ import annotations

from typing import List, Optional

from adapters.repository import AbstractSession, AbstractRepository
from adapters.repository.fake import FakeSession
from domain.entities.drawing import Drawing, DrawingCreate, DrawingUpdate


class FakeDrawingRepository(AbstractRepository):
    def __init__(self, session: FakeSession):
        super().__init__(session)
        self.session: AbstractSession = session
        self._pk_count = 1

    def __call__(self) -> FakeDrawingRepository:
        return self

    async def add(self, drawing_create: DrawingCreate) -> Drawing:
        drawing = Drawing(
            id=self._pk_count,
            **drawing_create.dict()
        )
        self._pk_count += 1
        return await self.session.add(drawing)

    async def get(self, id: int) -> Optional[Drawing]:
        return await self.session.get(lambda d: d.id == id)

    async def list(self) -> List[Drawing]:
        return await self.session.list()

    async def update(self, drawing_update: DrawingUpdate, id: int) -> Optional[Drawing]:
        return await self.session.update(
            entity=drawing_update,
            predicate=lambda d: d.id == id,
        )

    async def delete(self, id: int) -> bool:
        return await self.session.delete(lambda d: d.id == id)

    def _reload_pk(self) -> None:
        self._pk_count = 1

    async def clear(self) -> None:
        self._reload_pk()
        await self.session.clear()
