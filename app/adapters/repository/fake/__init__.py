from __future__ import annotations

from typing import Callable, Optional, List, Dict

from adapters.repository import AbstractSession, AbstractDatabase, AbstractMetadata, AbstractRepository
from domain.entities import AbstractEntity


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

    async def clear(self):
        self.data = []


class FakeMetadata(AbstractMetadata):
    pass


class FakeDatabase(AbstractDatabase):
    def __init__(self, metadata: AbstractMetadata, repositories: Dict[str, AbstractRepository]):
        self.metadata = metadata
        self.repositories = repositories

    async def truncate_database(self) -> None:
        for repository in self.repositories.values():
            await repository.clear()
