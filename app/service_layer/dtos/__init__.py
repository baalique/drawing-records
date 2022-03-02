from pydantic import BaseModel


class AbstractDtoOut(BaseModel):
    class Config:
        validate_assignment = True


class AbstractDtoCreate(BaseModel):
    class Config:
        validate_assignment = True


class AbstractDtoUpdate(BaseModel):
    class Config:
        validate_assignment = True
