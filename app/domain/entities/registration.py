from datetime import datetime

from pydantic import BaseModel

from app.domain.entities.drawing import Drawing


class Registration(BaseModel):
    id: int
    drawing: Drawing
    dt: datetime

    class Config:
        orm_mode = True


class RegistrationCreate(BaseModel):
    drawing: Drawing
    dt: datetime

    class Config:
        pass
