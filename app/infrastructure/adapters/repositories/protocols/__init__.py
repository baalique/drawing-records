from typing import Any, Dict, Generic, Iterable, Optional, TypeVar

from app.domain.entities import AbstractEntity

E = TypeVar("E", bound=AbstractEntity)


class Repository(Generic[E]):
    async def add(self, entity: E) -> E:
        ...

    async def get(self, id: int) -> Optional[E]:
        ...

    async def list(self) -> Iterable[E]:
        ...

    async def clear(self) -> None:
        ...


class WriteableRepository(Repository, Generic[E]):
    async def update(self, id: int, update_dict: Dict[str, Any]) -> Optional[E]:
        ...

    async def delete(self, id: int) -> bool:
        ...


class ReadOnlyRepository(Repository, Generic[E]):
    ...
