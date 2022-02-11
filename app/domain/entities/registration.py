from __future__ import annotations

from datetime import date

from pydantic import BaseModel

from app.domain.entities.drawing import Drawing


class Registration(BaseModel):
    id: int
    drawing: Drawing
    date: date

    class Config:
        orm_mode = True


class RegistrationCreate(Registration):
    pass

    class Config:
        pass
