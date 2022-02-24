from __future__ import annotations

from functools import partial
from typing import List, Optional

from app.adapters.repository import is_id_equals
from app.adapters.repository.fake import FakeSession
from app.adapters.repository.protocols.entities import DrawingRepository
from app.domain.entities.drawing import Drawing, DrawingCreate, DrawingUpdate


class FakeDrawingRepository(DrawingRepository):
    def __init__(self, session: FakeSession):
        self.session = session
        self.session.register_repository("Drawing", self)
        self._pk_count = 1

    async def add(self, drawing_create: DrawingCreate) -> Drawing:
        drawing = Drawing(id=self._pk_count, **drawing_create.dict())
        self._pk_count += 1
        return await self.session.add(drawing)

    async def get(self, id: int) -> Optional[Drawing]:
        drawings = await self.session.get(
            "Drawing",
            predicate=partial(is_id_equals, to=id),
        )
        return drawings[0] if drawings else None

    async def list(self) -> List[Drawing]:
        return await self.session.list("Drawing")

    async def update(self, drawing_update: DrawingUpdate, id: int) -> Optional[Drawing]:
        update_dict = {k: v for k, v in drawing_update.dict().items() if v is not None}

        updated = await self.session.update(
            "Drawing", predicate=partial(is_id_equals, to=id), **update_dict
        )
        return None if not updated else updated[0]

    async def delete(self, id: int) -> bool:
        return await self.session.delete(
            "Drawing", predicate=partial(is_id_equals, to=id)
        )

    async def clear(self) -> None:
        self._pk_count = 1
        await self.session.clear()
