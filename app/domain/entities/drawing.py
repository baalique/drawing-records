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


class DrawingCreate(BaseModel):
    name: str
    parent: Optional[Drawing]
    category: str
    project: str
    drawing_data: dict
    path_to_file: FilePath


class DrawingUpdate(BaseModel):
    name: Optional[str]
    parent: Optional[Drawing]
    category: Optional[str]
    project: Optional[str]
    drawing_data: Optional[dict]
    path_to_file: Optional[FilePath]
