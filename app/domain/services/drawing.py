from typing import Awaitable, Callable, Iterable, Optional

from app.service_layer.dtos.drawing import (
    DrawingDtoCreate,
    DrawingDtoOut,
    DrawingDtoUpdate,
)


async def create_drawing(
    create_one: Callable[[DrawingDtoCreate], Awaitable[DrawingDtoOut]],
    dto: DrawingDtoCreate,
) -> DrawingDtoOut:
    return await create_one(dto)


async def get_drawing_by_id(
    get_one: Callable[[int], Awaitable[Optional[DrawingDtoOut]]], id: int
) -> Optional[DrawingDtoOut]:
    return await get_one(id)


async def get_all_drawings(
    get_all: Callable[[], Awaitable[Iterable[DrawingDtoOut]]]
) -> Iterable[DrawingDtoOut]:
    return await get_all()


async def update_drawing(
    update_one: Callable[[DrawingDtoUpdate, int], Awaitable[Optional[DrawingDtoOut]]],
    dto: DrawingDtoUpdate,
    id: int,
) -> Optional[DrawingDtoOut]:
    return await update_one(dto, id)


async def delete_drawing(delete_one: Callable[[int], Awaitable[bool]], id: int) -> bool:
    return await delete_one(id)
