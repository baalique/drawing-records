from typing import List, Optional

from app.infrastructure.protocols import UnitOfWork
from app.service_layer.dtos.drawing import (
    DrawingDtoCreate,
    DrawingDtoOut,
    DrawingDtoUpdate,
)
from app.service_layer.exceptions import AlreadyExistsError, NotFoundError


async def create_drawing(
    drawing_create: DrawingDtoCreate, uow: UnitOfWork
) -> DrawingDtoOut:
    async with uow:
        exists = await id_exists(drawing_create.id, uow)
        if exists:
            raise AlreadyExistsError(
                f"Drawing with id {drawing_create.id} already exists"
            )

        if drawing_create.parent_id is None:
            parent = None
        else:
            parent = await uow.drawings.get(drawing_create.parent_id)
            if not parent:
                raise NotFoundError(
                    f"Drawing with id {drawing_create.parent_id} not found"
                )

        drawing = drawing_create.to_entity(parent)
        result = await uow.drawings.add(drawing)
        dto_out = DrawingDtoOut.from_entity(result)

        await uow.commit()

        return dto_out


async def get_drawing_by_id(id: int, uow: UnitOfWork) -> DrawingDtoOut:
    async with uow:
        result = await uow.drawings.get(id)
        if not result:
            raise NotFoundError(f"Drawing with id {id} not found")

        return DrawingDtoOut.from_entity(result)


async def get_all_drawings(uow: UnitOfWork) -> List[DrawingDtoOut]:
    async with uow:
        drawings = await uow.drawings.list()

        return list(map(DrawingDtoOut.from_entity, drawings))


async def update_drawing(
    id: int, drawing_update: DrawingDtoUpdate, uow: UnitOfWork
) -> Optional[DrawingDtoOut]:
    async with uow:
        exists = await id_exists(id, uow)
        if not exists:
            raise NotFoundError(f"Drawing with id {drawing_update.parent_id} not found")
        exists = await id_exists(drawing_update.id, uow)
        if exists and id != drawing_update.id:
            raise AlreadyExistsError(
                f"Drawing with id {drawing_update.id} already exists"
            )
        exists = await id_exists(drawing_update.parent_id, uow)
        if drawing_update.parent_id is not None and not exists:
            raise NotFoundError(f"Drawing with id {drawing_update.parent_id} not found")

        old_drawing = await get_drawing_by_id(id, uow)
        update_dict = old_drawing.dict() | {
            k: v
            for k, v in drawing_update.dict().items()
            if v is not None or k == "parent_id"
        }

        drawing = await uow.drawings.update(id, update_dict=update_dict)

        await uow.commit()

        return DrawingDtoOut.from_entity(drawing) if drawing else None


async def delete_drawing(id: int, uow: UnitOfWork) -> bool:
    async with uow:
        exists = await id_exists(id, uow)
        if not exists:
            raise NotFoundError(f"Drawing with id {id} not found")

        result = await uow.drawings.delete(id)

        await uow.commit()

        return result


async def id_exists(id: Optional[int], uow: UnitOfWork) -> bool:
    async with uow:
        if id is None:
            return False

        all_drawings = await get_all_drawings(uow)

        return id in (d.id for d in all_drawings)
