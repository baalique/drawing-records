import abc
from typing import List, Optional

from domain.entities import AbstractEntity


class AbstractSession(abc.ABC):
    @abc.abstractmethod
    async def add(self, entity: AbstractEntity) -> AbstractEntity:
        raise NotImplementedError

    @abc.abstractmethod
    async def get(self, *args, **kwargs) -> Optional[AbstractEntity]:
        raise NotImplementedError

    @abc.abstractmethod
    async def list(self) -> List[AbstractEntity]:
        raise NotImplementedError

    @abc.abstractmethod
    async def update(self, *args, **kwargs) -> Optional[AbstractEntity]:
        raise NotImplementedError

    @abc.abstractmethod
    async def delete(self, *args, **kwargs) -> bool:
        raise NotImplementedError

    @abc.abstractmethod
    async def clear(self) -> None:
        raise NotImplementedError


class AbstractRepository(abc.ABC):
    def __init__(self, session: AbstractSession):
        self.session = session

    @abc.abstractmethod
    async def add(self, entity: AbstractEntity) -> AbstractEntity:
        raise NotImplementedError

    @abc.abstractmethod
    async def get(self, *args, **kwargs) -> Optional[AbstractEntity]:
        raise NotImplementedError

    @abc.abstractmethod
    async def list(self) -> List[AbstractEntity]:
        raise NotImplementedError

    async def update(self, *args, **kwargs) -> Optional[AbstractEntity]:
        pass

    async def delete(self, *args, **kwargs) -> bool:
        pass

    @abc.abstractmethod
    async def clear(self) -> None:
        raise NotImplementedError


class AbstractMetadata(abc.ABC):
    pass


class AbstractDatabase(abc.ABC):
    @abc.abstractmethod
    async def truncate_database(self) -> None:
        raise NotImplementedError
