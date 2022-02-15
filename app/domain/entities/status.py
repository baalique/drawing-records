from pydantic import BaseModel


class Status(BaseModel):
    title: str
    description: str
    version: str
