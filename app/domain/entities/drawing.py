from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, FilePath


class Drawing(BaseModel):
    id: int
    name: str
    parent: Optional[Drawing]
    category: str
    project: str
    drawing_data: dict
    path_to_file: FilePath

    class Config:
        orm_mode = True


class DrawingCreate(Drawing):
    pass

    class Config:
        pass


class DrawingUpdate(Drawing):
    pass

    class Config:
        pass
