from app.service_layer.dtos import AbstractDtoOut


class Status(AbstractDtoOut):
    title: str
    description: str
    version: str
