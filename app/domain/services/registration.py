from datetime import datetime
from typing import Callable, Iterable

from app.domain.entities.drawing import Drawing
from app.domain.entities.registration import Registration


def create_registration(create_one: Callable[[Drawing, datetime], Registration],
                        drawing: Drawing, dt: datetime) -> Registration:
    return create_one(drawing, dt)


def get_registration(get_one: Callable[[int], Registration], id: int) -> Registration:
    return get_one(id)


def get_all_registrations(get_all: Callable[[], Iterable[Registration]]) -> Iterable[Registration]:
    return get_all()


def delete_registration(delete_one: Callable[[int], bool], id: int) -> bool:
    return delete_one(id)
