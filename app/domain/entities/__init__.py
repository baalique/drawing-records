from pydantic import BaseModel


class AbstractEntity(BaseModel):
    pass


class AbstractEntityCreate(BaseModel):
    pass


class AbstractEntityUpdate(BaseModel):
    pass
