from typing import Generic, Iterable, Optional, TypeVar

from app.domain.entities import AbstractEntity
from app.service_layer.dtos import AbstractDtoCreate, AbstractDtoUpdate

E = TypeVar("E", bound=AbstractEntity)
EC = TypeVar("EC", bound=AbstractDtoCreate)
EU = TypeVar("EU", bound=AbstractDtoUpdate)


class Repository(Generic[E, EC]):
    async def add(self, entity: E) -> E:
        ...

    async def get(self, id: int) -> Optional[E]:
        ...

    async def list(self) -> Iterable[E]:
        ...

    async def clear(self) -> None:
        ...


class WriteableRepository(Repository, Generic[E, EC, EU]):
    async def update(self, entity: EU, id: int) -> E:
        ...

    async def delete(self, id: int) -> bool:
        ...


class ReadOnlyRepository(Repository, Generic[E, EC]):
    ...
