import abc

from app.domain.entities.protocols import HasId


class AbstractMetadata(abc.ABC):
    pass


class AbstractDatabase(abc.ABC):
    @abc.abstractmethod
    async def truncate_database(self) -> None:
        raise NotImplementedError


def is_id_equals(entity: HasId, to: int) -> bool:
    return entity.id == to
