from __future__ import annotations

from typing import List, Callable, Optional

from adapters.repository import AbstractSession, AbstractRepository
from domain.entities import AbstractEntity
from domain.entities.drawing import Drawing, DrawingCreate, DrawingUpdate


class FakeSession(AbstractSession):
    def __init__(self):
        self.data = []

    async def add(self, entity: AbstractEntity) -> AbstractEntity:
        self.data.append(entity)
        return entity

    async def get(self, predicate: Callable[[AbstractEntity], bool]) -> Optional[AbstractEntity]:
        for entity in self.data:
            if predicate(entity):
                return entity

    async def list(self) -> List[AbstractEntity]:
        return self.data

    async def update(self, entity: AbstractEntity, predicate: Callable[[AbstractEntity], bool]) \
            -> Optional[AbstractEntity]:
        for idx, e in enumerate(self.data):
            if predicate(e):
                update_data = entity.dict(exclude_unset=True)
                updated_entity = e.copy(update=update_data)
                self.data[idx] = updated_entity
                return updated_entity

    async def delete(self, predicate: Callable[[AbstractEntity], bool]) -> bool:
        for entity in self.data:
            if predicate(entity):
                self.data.remove(entity)
                return True
        return False


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
