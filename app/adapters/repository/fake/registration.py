from __future__ import annotations

from typing import List, Optional

from adapters.exceptions.exceptions import RelatedEntityNotExistsException
from adapters.repository.fake import FakeSession, FakeBaseRepository
from domain.entities import AbstractEntity
from domain.entities.registration import Registration, RegistrationCreate


class FakeRegistrationRepository(FakeBaseRepository):
    def __init__(self, session: FakeSession):
        super().__init__(session)
        self.session.register_repository("Registration", self)

    async def add(self, registration_create: RegistrationCreate) -> Registration:
        drawings = await self.session.get("Drawing", predicate=lambda d: d.id == registration_create.drawing_id)
        if not drawings:
            raise RelatedEntityNotExistsException(
                f"Cannot find drawing with id={registration_create.drawing_id}")

        registration = Registration(
            id=self._pk_count,
            drawing=drawings[0],
            created_at=registration_create.created_at
        )
        self._pk_count += 1
        return await self.session.add(registration)

    async def get(self, id: int) -> Optional[AbstractEntity]:
        registrations = await self.session.get("Registration", lambda d: d.id == id)
        return registrations[0] if registrations else None

    async def list(self) -> List[AbstractEntity]:
        return await self.session.list("Registration")
