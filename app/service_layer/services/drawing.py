from typing import List, Optional

from app.infrastructure.adapters.repositories.protocols.entities import (
    DrawingRepository,
)
from app.service_layer.dtos.drawing import (
    DrawingDtoCreate,
    DrawingDtoOut,
    DrawingDtoUpdate,
)
from app.service_layer.exceptions import AlreadyExistsError, NotFoundError


async def create_drawing(
    drawing_create: DrawingDtoCreate, repo: DrawingRepository
) -> DrawingDtoOut:
    exists = await id_exists(drawing_create.id, repo)
    if exists:
        raise AlreadyExistsError(f"Drawing with id {drawing_create.id} already exists")

    if drawing_create.parent_id is None:
        parent = None
    else:
        parent = await repo.get(drawing_create.parent_id)
        if not parent:
            raise NotFoundError(f"Drawing with id {drawing_create.parent_id} not found")

    drawing = drawing_create.to_entity(parent)
    result = await repo.add(drawing)
    dto_out = DrawingDtoOut.from_entity(result)
    return dto_out


async def get_drawing_by_id(id: int, repo: DrawingRepository) -> DrawingDtoOut:
    result = await repo.get(id)
    if not result:
        raise NotFoundError(f"Drawing with id {id} not found")
    return DrawingDtoOut.from_entity(result)


async def get_all_drawings(repo: DrawingRepository) -> List[DrawingDtoOut]:
    drawings = await repo.list()
    return list(map(DrawingDtoOut.from_entity, drawings))


async def update_drawing(
    id: int, drawing_update: DrawingDtoUpdate, repo: DrawingRepository
) -> Optional[DrawingDtoOut]:
    exists = await id_exists(id, repo)
    if not exists:
        raise NotFoundError(f"Drawing with id {drawing_update.parent_id} not found")
    exists = await id_exists(drawing_update.id, repo)
    if exists and id != drawing_update.id:
        raise AlreadyExistsError(f"Drawing with id {drawing_update.id} already exists")
    exists = await id_exists(drawing_update.parent_id, repo)
    if drawing_update.parent_id is not None and not exists:
        raise NotFoundError(f"Drawing with id {drawing_update.parent_id} not found")

    old_drawing = await get_drawing_by_id(id, repo)
    update_dict = old_drawing.dict() | {
        k: v
        for k, v in drawing_update.dict().items()
        if v is not None or k == "parent_id"
    }

    drawing = await repo.update(id, update_dict=update_dict)

    return DrawingDtoOut.from_entity(drawing) if drawing else None


async def delete_drawing(id: int, repo: DrawingRepository) -> bool:
    exists = await id_exists(id, repo)
    if not exists:
        raise NotFoundError(f"Drawing with id {id} not found")

    result = await repo.delete(id)
    return result


async def id_exists(id: Optional[int], repo: DrawingRepository) -> bool:
    if id is None:
        return False
    all_drawings = await get_all_drawings(repo)
    return id in (d.id for d in all_drawings)
