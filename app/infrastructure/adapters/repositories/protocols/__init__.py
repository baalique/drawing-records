from typing import Callable, Generic, Iterable, List, Optional, Protocol, TypeVar

from app.service_layer.dtos import AbstractDtoCreate, AbstractDtoOut, AbstractDtoUpdate

E = TypeVar("E", bound=AbstractDtoOut)
EC = TypeVar("EC", bound=AbstractDtoCreate)
EU = TypeVar("EU", bound=AbstractDtoUpdate)


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


class Repository(Generic[E, EC]):
    async def add(self, entity: EC) -> E:
        ...

    async def get(self, id: int) -> Optional[E]:
        ...

    async def list(self) -> Iterable[E]:
        ...

    async def clear(self) -> None:
        ...


class WriteableRepository(Repository, Generic[E, EC, EU]):
    async def update(self, entity: EU, id: int) -> Optional[E]:
        ...

    async def delete(self, id: int) -> bool:
        ...


class ReadOnlyRepository(Repository, Generic[E, EC]):
    ...
