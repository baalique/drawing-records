from typing import Callable, Optional, Iterable, Awaitable

from app.domain.entities.drawing import DrawingCreate, Drawing, DrawingUpdate


async def create_drawing(create_one: Callable[[DrawingCreate], Awaitable[Drawing]], dto: DrawingCreate) -> Drawing:
    return await create_one(dto)


async def get_drawing_by_id(get_one: Callable[[int], Awaitable[Drawing]], id: int) -> Drawing:
    return await get_one(id)


async def get_all_drawings(get_all: Callable[[], Awaitable[Iterable[Drawing]]]) -> Iterable[Drawing]:
    return await get_all()


async def update_drawing(update_one: Callable[[DrawingUpdate, int], Awaitable[Optional[Drawing]]],
                         dto: DrawingUpdate, id: int) -> Optional[Drawing]:
    return await update_one(dto, id)


async def delete_drawing(delete_one: Callable[[int], Awaitable[bool]], id: int) -> bool:
    return await delete_one(id)
