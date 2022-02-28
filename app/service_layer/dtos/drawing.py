from __future__ import annotations

from pathlib import Path
from typing import Optional

from app.service_layer.dtos import AbstractDtoCreate, AbstractDtoOut, AbstractDtoUpdate


class DrawingDtoOut(AbstractDtoOut):
    id: int
    name: str
    parent: Optional[DrawingDtoOut]
    category: str
    project: str
    drawing_data: dict
    path_to_file: Path


class DrawingDtoCreate(AbstractDtoCreate):
    name: str
    parent_id: Optional[int]
    category: str
    project: str
    drawing_data: dict
    path_to_file: Path


class DrawingDtoUpdate(AbstractDtoUpdate):
    name: Optional[str]
    parent_id: Optional[int]
    category: Optional[str]
    project: Optional[str]
    drawing_data: Optional[dict]
    path_to_file: Optional[Path]
