from typing import Callable, Optional, Iterable

from app.domain.entities.drawing import DrawingCreate, Drawing, DrawingUpdate


def create_drawing(create_one: Callable[[DrawingCreate], Drawing], dto: DrawingCreate) -> Drawing:
    return create_one(dto)


def get_drawing_by_id(get_one: Callable[[int], Drawing], id: int) -> Drawing:
    return get_one(id)


def get_all_drawings(get_all: Callable[[], Iterable[Drawing]]) -> Iterable[Drawing]:
    return get_all()


def update_drawing(update_one: Callable[[DrawingUpdate, int], Optional[Drawing]], dto: DrawingUpdate, id: int) \
        -> Optional[Drawing]:
    return update_one(dto, id)


def delete_drawing(delete_one: Callable[[int], bool], id: int) -> bool:
    return delete_one(id)
