from __future__ import annotations

from typing import Optional, Any

from app.domain.entities import AbstractEntity


class Drawing(AbstractEntity):
    def __init__(
        self,
        id: int,
        name: str,
        parent: Optional[Drawing],
        category: str,
        project: str,
        drawing_data: dict,
        path_to_file: str,
    ):
        self.id = id
        self.name = name
        self.parent = parent
        self.parent_id = None if parent is None else parent.id
        self.category = category
        self.project = project
        self.drawing_data = drawing_data
        self.path_to_file = path_to_file

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, Drawing) and self.id == other.id
