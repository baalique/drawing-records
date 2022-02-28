from typing import Awaitable, Callable, Iterable, Optional

from app.service_layer.dtos.registration import RegistrationCreate, RegistrationDtoOut


async def create_registration(
    create_one: Callable[[RegistrationCreate], Awaitable[RegistrationDtoOut]],
    dto: RegistrationCreate,
) -> RegistrationDtoOut:
    return await create_one(dto)


async def get_registration_by_id(
    get_one: Callable[[int], Awaitable[Optional[RegistrationDtoOut]]], id: int
) -> Optional[RegistrationDtoOut]:
    return await get_one(id)


async def get_all_registrations(
    get_all: Callable[[], Awaitable[Iterable[RegistrationDtoOut]]]
) -> Iterable[RegistrationDtoOut]:
    return await get_all()


async def delete_registration(
    delete_one: Callable[[int], Awaitable[bool]], id: int
) -> bool:
    return await delete_one(id)
