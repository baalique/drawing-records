from __future__ import annotations

from pathlib import Path
from typing import Optional

from app.domain.entities import (
    AbstractEntity,
    AbstractEntityCreate,
    AbstractEntityUpdate,
)


class Drawing(AbstractEntity):
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


class DrawingCreate(AbstractEntityCreate):
    name: str
    parent_id: Optional[int]
    category: str
    project: str
    drawing_data: dict
    path_to_file: Path


class DrawingUpdate(AbstractEntityUpdate):
    name: Optional[str]
    parent_id: Optional[int]
    category: Optional[str]
    project: Optional[str]
    drawing_data: Optional[dict]
    path_to_file: Optional[Path]
