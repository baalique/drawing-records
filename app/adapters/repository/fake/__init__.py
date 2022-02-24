from __future__ import annotations

from typing import Callable, Dict, List, TypeVar

from app.adapters.exceptions.exceptions import InvalidEntityException
from app.adapters.repository import AbstractDatabase, AbstractMetadata
from app.adapters.repository.protocols import Repository, Session
from app.domain.entities import AbstractEntity

E = TypeVar("E", bound=AbstractEntity)


class FakeSession(Session):
    def __init__(self):
        self.data: Dict[str, List[E]] = {}
        self._repositories: Dict[str, Repository] = {}

    def register_repository(self, model: str, repository: Repository) -> None:
        self.data[model] = []
        self._repositories[model] = repository

    async def add(self, entity: E) -> E:
        type_ = type(entity)
        if not self._has_model(type_.__name__):
            raise InvalidEntityException(f"Cannot add entity with type {type_}")
        self.data[type_.__name__].append(entity)
        return entity

    async def get(self, model: str, predicate: Callable[[E], bool]) -> List[E]:
        if not self._has_model(model):
            raise InvalidEntityException(f"Cannot get entity with type {model}")

        return list(filter(predicate, self.data[model]))

    async def list(self, model: str) -> List[E]:
        if not self._has_model(model):
            raise InvalidEntityException(f"Cannot get entities with type {model}")
        return self.data[model]

    async def update(
        self, model: str, predicate: Callable[[E], bool], **kwargs
    ) -> List[E]:
        if not self._has_model(model):
            raise InvalidEntityException(f"Cannot update entities with type {model}")

        res = []

        for idx, e in enumerate(self.data[model]):
            if predicate(e):
                updated_entity = e.copy(update=kwargs)
                self.data[model][idx] = updated_entity
                res.append(updated_entity)

        return res

    async def delete(self, model: str, predicate: Callable[[E], bool]) -> bool:
        if not self._has_model(model):
            raise InvalidEntityException(f"Cannot delete entities with type {model}")

        start_len = len(self.data[model])

        self.data[model] = list(filter(lambda e: not predicate(e), self.data[model]))

        return start_len != len(self.data[model])

    async def clear(self) -> None:
        self.data = {type_: [] for type_ in self.data}

    def _has_model(self, model: str) -> bool:
        return model in self.data

    def close(self) -> None:
        pass


class FakeMetadata(AbstractMetadata):
    pass


class FakeDatabase(AbstractDatabase):
    def __init__(self, metadata: AbstractMetadata, repositories: Dict[str, Repository]):
        self.metadata = metadata
        self.repositories = repositories

    async def truncate_database(self) -> None:
        for repository in self.repositories.values():
            await repository.clear()

    def close(self) -> None:
        pass
