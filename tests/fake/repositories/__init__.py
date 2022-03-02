from __future__ import annotations

import abc
from typing import Callable, Dict, List, Protocol, TypeVar

from app.domain.entities import AbstractEntity
from app.infrastructure.adapters.repositories.protocols import Repository
from tests.fake.exceptions import FakeInvalidEntityError


class AbstractDatabase(abc.ABC):
    @abc.abstractmethod
    async def truncate_database(self) -> None:
        raise NotImplementedError


E = TypeVar("E", bound=AbstractEntity)


class Session(Protocol):
    async def add(self, entity: E) -> E:
        ...

    async def get(self, model: str, predicate: Callable[[E], bool]) -> List[E]:
        ...

    async def list(self, model: str) -> List[E]:
        ...

    async def update(
        self, model: str, predicate: Callable[[E], bool], **kwargs
    ) -> List[E]:
        ...

    async def delete(self, model: str, predicate: Callable[[E], bool]) -> bool:
        ...


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
            raise FakeInvalidEntityError(f"Cannot add entity with type {type_}")
        self.data[type_.__name__].append(entity)
        return entity

    async def get(self, model: str, predicate: Callable[[E], bool]) -> List[E]:
        if not self._has_model(model):
            raise FakeInvalidEntityError(f"Cannot get entity with type {model}")

        return list(filter(predicate, self.data[model]))

    async def list(self, model: str) -> List[E]:
        if not self._has_model(model):
            raise FakeInvalidEntityError(f"Cannot get entities with type {model}")
        return self.data[model]

    async def update(
        self, model: str, predicate: Callable[[E], bool], **kwargs
    ) -> List[E]:
        if not self._has_model(model):
            raise FakeInvalidEntityError(f"Cannot update entities with type {model}")

        res = []

        data: List[E] = self.data[model]

        for e in data:
            if predicate(e):
                for k, v in kwargs.items():
                    setattr(e, k, v)
                res.append(e)

        return res

    async def delete(self, model: str, predicate: Callable[[E], bool]) -> bool:
        if not self._has_model(model):
            raise FakeInvalidEntityError(f"Cannot delete entities with type {model}")

        start_len = len(self.data[model])

        self.data[model] = list(filter(lambda e: not predicate(e), self.data[model]))

        return start_len != len(self.data[model])

    async def clear(self) -> None:
        self.data = {type_: [] for type_ in self.data}

    def _has_model(self, model: str) -> bool:
        return model in self.data

    def close(self) -> None:
        pass


class FakeDatabase(AbstractDatabase):
    def __init__(self, repositories: Dict[str, Repository]):
        self.repositories = repositories

    async def truncate_database(self) -> None:
        for repository in self.repositories.values():
            await repository.clear()

    def close(self) -> None:
        pass
