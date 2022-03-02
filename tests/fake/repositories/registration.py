from __future__ import annotations

from functools import partial
from typing import List, Optional

from app.infrastructure.adapters.repositories import is_id_equals
from app.infrastructure.adapters.repositories.protocols.entities import (
    RegistrationRepository,
)
from app.service_layer.dtos.registration import (
    RegistrationDtoCreate,
    RegistrationDtoOut,
)
from tests.fake.exceptions import FakeRelatedEntityNotExistsError
from tests.fake.repositories import FakeSession


class FakeRegistrationRepository(RegistrationRepository):
    def __init__(self, session: FakeSession):
        self.session = session
        self.session.register_repository("Registration", self)
        self._pk_count = 1

    async def add(
        self, registration_create: RegistrationDtoCreate
    ) -> RegistrationDtoOut:
        drawings = await self.session.get(
            "Drawing",
            predicate=partial(is_id_equals, to=registration_create.drawing_id),
        )
        if not drawings:
            raise FakeRelatedEntityNotExistsError(
                f"Cannot find drawing with id={registration_create.drawing_id}"
            )

        registration = RegistrationDtoOut(
            id=self._pk_count,
            drawing=drawings[0],
            created_at=registration_create.created_at,
        )
        self._pk_count += 1
        return await self.session.add(registration)

    async def get(self, id: int) -> Optional[RegistrationDtoOut]:
        registrations = await self.session.get(
            "Registration", predicate=partial(is_id_equals, to=id)
        )
        return registrations[0] if registrations else None

    async def list(self) -> List[RegistrationDtoOut]:
        return await self.session.list("Registration")

    async def clear(self) -> None:
        self._pk_count = 1
        await self.session.clear()
