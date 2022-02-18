from __future__ import annotations

from typing import Optional

from adapters.repository.fake import FakeSession, FakeBaseRepository
from domain.entities.drawing import Drawing, DrawingCreate, DrawingUpdate


class FakeDrawingRepository(FakeBaseRepository):
    def __init__(self, session: FakeSession):
        super().__init__(session)

    async def add(self, drawing_create: DrawingCreate) -> Drawing:
        drawing = Drawing(
            id=self._pk_count,
            **drawing_create.dict()
        )
        self._pk_count += 1
        return await self.session.add(drawing)

    async def update(self, drawing_update: DrawingUpdate, id: int) -> Optional[Drawing]:
        return await self.session.update(
            entity=drawing_update,
            predicate=lambda d: d.id == id,
        )

    async def delete(self, id: int) -> bool:
        return await self.session.delete(lambda d: d.id == id)
