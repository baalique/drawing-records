from datetime import datetime

from app.domain.entities import AbstractEntity, AbstractEntityCreate
from app.domain.entities.drawing import Drawing


class Registration(AbstractEntity):
    id: int
    drawing: Drawing
    created_at: datetime

    class Config:
        orm_mode = True
        validate_assignment = True


class RegistrationCreate(AbstractEntityCreate):
    drawing_id: int
    created_at: datetime
