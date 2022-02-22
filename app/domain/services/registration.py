from typing import Awaitable, Callable, Iterable

from app.domain.entities.registration import Registration, RegistrationCreate


async def create_registration(
    create_one: Callable[[RegistrationCreate], Awaitable[Registration]],
    dto: RegistrationCreate,
) -> Registration:
    return await create_one(dto)


async def get_registration_by_id(
    get_one: Callable[[int], Awaitable[Registration]], id: int
) -> Registration:
    return await get_one(id)


async def get_all_registrations(
    get_all: Callable[[], Awaitable[Iterable[Registration]]]
) -> Iterable[Registration]:
    return await get_all()


async def delete_registration(
    delete_one: Callable[[int], Awaitable[bool]], id: int
) -> bool:
    return await delete_one(id)
