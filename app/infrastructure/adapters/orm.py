from sqlalchemy import Column, ForeignKey, Integer, MetaData, Table, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import registry  # type: ignore

from app.domain.entities.drawing import Drawing

metadata = MetaData()
mapper_registry = registry()

drawing_table = Table(
    "drawing",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", Text()),
    Column("parent_id", Integer, ForeignKey("drawing.id")),
    Column("category", Text()),
    Column("project", Text()),
    Column("drawing_data", JSONB),
    Column("path_to_file", Text()),
)


def start_mappers() -> None:
    mapper_registry.map_imperatively(
        Drawing,
        drawing_table,
        properties={
            "id": drawing_table.c.id,
            "name": drawing_table.c.name,
            "parent_id": drawing_table.c.parent_id,
            "category": drawing_table.c.category,
            "project": drawing_table.c.project,
            "drawing_data": drawing_table.c.drawing_data,
            "path_to_file": drawing_table.c.path_to_file,
        },
    )
