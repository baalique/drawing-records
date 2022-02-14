from __future__ import annotations

from pathlib import Path
from typing import Optional

from pydantic import BaseModel


class Drawing(BaseModel):
    id: int
    name: str
    parent: Optional[Drawing]
    category: str
    project: str
    drawing_data: dict
    path_to_file: Path

    class Config:
        orm_mode = True
        validate_assignment = True


class DrawingCreate(BaseModel):
    name: str
    parent_id: Optional[int]
    category: str
    project: str
    drawing_data: dict
    path_to_file: Path


class DrawingUpdate(BaseModel):
    name: Optional[str]
    parent_id: Optional[int]
    category: Optional[str]
    project: Optional[str]
    drawing_data: Optional[dict]
    path_to_file: Optional[Path]
