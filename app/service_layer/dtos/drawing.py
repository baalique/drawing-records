from __future__ import annotations

from typing import Optional

from pydantic import Field

from app.domain.entities.drawing import Drawing
from app.service_layer.dtos import AbstractDtoCreate, AbstractDtoOut, AbstractDtoUpdate


class DrawingDtoOut(AbstractDtoOut):
    id: int
    name: str
    parent_id: Optional[int] = Field(...)
    category: str
    project: str
    drawing_data: dict
    path_to_file: str

    @staticmethod
    def from_entity(drawing: Drawing) -> DrawingDtoOut:
        return DrawingDtoOut(
            id=drawing.id,
            name=drawing.name,
            parent_id=drawing.parent_id,
            category=drawing.category,
            project=drawing.project,
            drawing_data=drawing.drawing_data,
            path_to_file=drawing.path_to_file,
        )


class DrawingDtoCreate(AbstractDtoCreate):
    id: int
    name: str
    parent_id: Optional[int] = Field(...)
    category: str
    project: str
    drawing_data: dict
    path_to_file: str

    def to_entity(self, parent: Optional[Drawing]) -> Drawing:
        return Drawing(
            id=self.id,
            name=self.name,
            parent=parent,
            category=self.category,
            project=self.project,
            drawing_data=self.drawing_data,
            path_to_file=str(self.path_to_file),
        )


class DrawingDtoUpdate(AbstractDtoUpdate):
    id: Optional[int]
    name: Optional[str]
    parent_id: Optional[int]
    category: Optional[str]
    project: Optional[str]
    drawing_data: Optional[dict]
    path_to_file: Optional[str]
