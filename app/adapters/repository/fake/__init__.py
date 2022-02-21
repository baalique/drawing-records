from __future__ import annotations

import abc
from typing import Callable, Optional, List, Dict

from adapters.exceptions.exceptions import InvalidEntityException
from adapters.repository import AbstractSession, AbstractDatabase, AbstractMetadata, AbstractRepository
from domain.entities import AbstractEntity


class FakeSession(AbstractSession):
    def __init__(self):
        self.data: Dict[str, List[AbstractEntity]] = {}
        self._repositories: Dict[str, AbstractRepository] = {}

    def register_repository(self, model: str, repository: AbstractRepository):
        self.data[model] = []
        self._repositories[model] = repository

    async def add(self, entity: AbstractEntity) -> AbstractEntity:
        type_ = type(entity)
        if not self._has_model(type_.__name__):
            raise InvalidEntityException(f"Cannot add entity with type {type_}")
        self.data[type_.__name__].append(entity)
        return entity

    async def get(self, model: str, predicate: Callable[[AbstractEntity], bool]) -> List[AbstractEntity]:
        if not self._has_model(model):
            raise InvalidEntityException(f"Cannot get entity with type {model}")

        return list(filter(predicate, self.data[model]))

    async def list(self, model: str) -> List[AbstractEntity]:
        if not self._has_model(model):
            raise InvalidEntityException(f"Cannot get entities with type {model}")
        return self.data[model]

    async def update(self, model: str, entity: AbstractEntity, predicate: Callable[[AbstractEntity], bool]) \
            -> Optional[AbstractEntity]:
        if not self._has_model(model):
            raise InvalidEntityException(f"Cannot update entities with type {model}")
        for idx, e in enumerate(self.data[model]):
            if predicate(e):
                update_data = entity.dict(exclude_unset=True)
                updated_entity = e.copy(update=update_data)
                self.data[model][idx] = updated_entity
                return updated_entity

    async def delete(self, model: str, predicate: Callable[[AbstractEntity], bool]) -> bool:
        if not self._has_model(model):
            raise InvalidEntityException(f"Cannot delete entities with type {model}")

        start_len = len(self.data[model])

        self.data[model] = list(filter(lambda e: not predicate(e), self.data[model]))

        return start_len != len(self.data[model])

    async def clear(self) -> None:
        self.data = {type_: [] for type_ in self.data}

    def _has_model(self, model: str) -> bool:
        return model in self.data

    def close(self):
        pass


class FakeMetadata(AbstractMetadata):
    pass


class FakeDatabase(AbstractDatabase):
    def __init__(self, metadata: AbstractMetadata, repositories: Dict[str, AbstractRepository]):
        self.metadata = metadata
        self.repositories = repositories

    async def truncate_database(self) -> None:
        for repository in self.repositories.values():
            await repository.clear()

    def close(self) -> None:
        pass


class FakeBaseRepository(AbstractRepository, abc.ABC):
    def __init__(self, session: FakeSession):
        self.session = session
        self._pk_count = 1

    def __call__(self) -> FakeBaseRepository:
        return self

    @abc.abstractmethod
    async def add(self, entity: AbstractEntity) -> AbstractEntity:
        raise NotImplementedError

    @abc.abstractmethod
    async def get(self, *args, **kwargs) -> Optional[AbstractEntity]:
        raise NotImplementedError

    @abc.abstractmethod
    async def list(self, *args, **kwargs) -> List[AbstractEntity]:
        raise NotImplementedError

    async def clear(self) -> None:
        self._reload_pk()
        await self.session.clear()

    def _reload_pk(self) -> None:
        self._pk_count = 1
