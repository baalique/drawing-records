from typing import Callable

import pytest

from adapters.repository.fake import FakeSession
from adapters.repository.fake.drawing import FakeDrawingRepository
from adapters.repository.fake.registration import FakeRegistrationRepository
from db import get_db
from domain.entities.registration import RegistrationCreate


@pytest.fixture(name="fake_session")
def fake_session_fixture() -> FakeSession:
    return list(get_db().repositories.values())[0].session


@pytest.fixture(name="drawing_repository_empty")
def drawing_repository_empty_fixture() -> FakeDrawingRepository:
    return get_db().repositories["Drawing"]


@pytest.fixture(name="drawing_repository")
async def drawing_repository_fixture(create_many_drawings_dto) -> FakeDrawingRepository:
    repository = get_db().repositories["Drawing"]
    for drawing in create_many_drawings_dto():
        await repository.add(drawing)
    return repository


@pytest.fixture(name="registration_repository_empty")
def registration_repository_empty_fixture() -> FakeRegistrationRepository:
    return get_db().repositories["Registration"]


@pytest.fixture(name="registration_repository")
def registration_repository_fixture(registrations) -> Callable[[int], FakeRegistrationRepository]:
    def get_repository(amount=10):
        all_registrations = registrations(amount)
        registration_repository = get_db().repositories["Registration"]

        drawings = [r.drawing for r in all_registrations]

        registration_repository.session.data["Registration"] = all_registrations
        registration_repository.session.data["Drawing"] = drawings

        registration_repository._pk_count = max(r.id for r in all_registrations) + 1
        registration_repository.session._repositories["Drawing"]._pk_count = max(d.id for d in drawings) + 1

        return registration_repository

    return lambda amount=10: get_repository(amount)


@pytest.fixture(name="create_registration_dto_from_repository")
def create_registration_dto_from_repository_fixture(factory_registration_create) \
        -> Callable[[FakeRegistrationRepository], RegistrationCreate]:
    def get_dto(registration_repository):
        drawing_id = registration_repository.session.data["Drawing"][-1].id
        return RegistrationCreate(**factory_registration_create().dict() | {"drawing_id": drawing_id})

    return get_dto


@pytest.fixture(name="create_many_registrations_dtos_from_repository")
def create_many_registration_dtos_from_repository_fixture(factory_registration_create) \
        -> Callable[[FakeRegistrationRepository], RegistrationCreate]:
    def get_dtos(registration_repository):
        drawing_id = registration_repository.session.data["Drawing"][-1].id
        return RegistrationCreate(**factory_registration_create().dict() | {"drawing_id": drawing_id})

    return get_dtos
