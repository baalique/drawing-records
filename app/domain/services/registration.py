from typing import Callable, Iterable

from app.domain.entities.registration import Registration, RegistrationCreate


def create_registration(create_one: Callable[[RegistrationCreate], Registration],
                        dto: RegistrationCreate) -> Registration:
    return create_one(dto)


def get_registration_by_id(get_one: Callable[[int], Registration], id: int) -> Registration:
    return get_one(id)


def get_all_registrations(get_all: Callable[[], Iterable[Registration]]) -> Iterable[Registration]:
    return get_all()


def delete_registration(delete_one: Callable[[int], bool], id: int) -> bool:
    return delete_one(id)
