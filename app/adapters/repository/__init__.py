import abc


class AbstractMetadata(abc.ABC):
    pass


class AbstractDatabase(abc.ABC):
    @abc.abstractmethod
    async def truncate_database(self) -> None:
        raise NotImplementedError
