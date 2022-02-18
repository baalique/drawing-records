from __future__ import annotations

import abc
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


class FakeBaseRepository(AbstractRepository, abc.ABC):
    def __init__(self, session: AbstractSession):
        super().__init__(session)
        self._pk_count = 1

    def __call__(self) -> FakeBaseRepository:
        return self

    @abc.abstractmethod
    async def add(self, entity: AbstractEntity) -> AbstractEntity:
        raise NotImplementedError

    async def get(self, id: int, *args, **kwargs) -> Optional[AbstractEntity]:
        return await self.session.get(lambda d: d.id == id)

    async def list(self) -> List[AbstractEntity]:
        return await self.session.list()

    async def clear(self) -> None:
        self._reload_pk()
        await self.session.clear()

    def _reload_pk(self) -> None:
        self._pk_count = 1
