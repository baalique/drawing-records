from app.domain.entities import AbstractEntity


class Status(AbstractEntity):
    title: str
    description: str
    version: str
