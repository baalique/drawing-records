from datetime import datetime

from pydantic import BaseModel

from app.domain.entities.drawing import Drawing


class Registration(BaseModel):
    id: int
    drawing: Drawing
    created_at: datetime

    class Config:
        orm_mode = True
        validate_assignment = True


class RegistrationCreate(BaseModel):
    drawing_id: int
    created_at: datetime
