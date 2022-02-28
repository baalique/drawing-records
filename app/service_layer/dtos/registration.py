from datetime import datetime

from app.service_layer.dtos import AbstractDtoCreate, AbstractDtoOut
from app.service_layer.dtos.drawing import DrawingDtoOut


class RegistrationDtoOut(AbstractDtoOut):
    id: int
    drawing: DrawingDtoOut
    created_at: datetime


class RegistrationCreate(AbstractDtoCreate):
    drawing_id: int
    created_at: datetime
