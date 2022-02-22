from typing import Callable, List

import pytest
from adapters.repository.fake import FakeDatabase
from domain.entities.registration import Registration
from pytest_factoryboy import register

from tests.factories.entities.drawing import (
    FactoryDrawing,
    FactoryDrawingCreate,
    FactoryDrawingUpdate,
)
from tests.factories.entities.registration import (
    FactoryRegistration,
    FactoryRegistrationCreate,
)
from tests.utils import make_many

for factory in (
    FactoryDrawing,
    FactoryDrawingCreate,
    FactoryDrawingUpdate,
    FactoryRegistration,
    FactoryRegistrationCreate,
):
    register(factory)


@pytest.fixture(name="drawing")
def drawing_fixture(factory_drawing):
    return factory_drawing()


@pytest.fixture(name="drawings")
def drawings_fixture(factory_drawing, default_database_size):
    return lambda amount=default_database_size: make_many(factory_drawing, amount)


@pytest.fixture(name="create_drawing_dto")
def create_drawing_dto_fixture(factory_drawing_create):
    return factory_drawing_create()


@pytest.fixture(name="create_many_drawings_dto")
def create_many_drawings_dto_fixture(factory_drawing_create, default_database_size):
    return lambda amount=default_database_size: make_many(
        factory_drawing_create, amount
    )


@pytest.fixture(name="update_drawing_dto")
def update_drawing_dto_fixture(factory_drawing_update):
    return factory_drawing_update()


@pytest.fixture(name="registration")
def registration_fixture(factory_registration):
    return factory_registration()


@pytest.fixture(name="registrations")
def registrations_fixture(factory_registration, default_database_size):
    return lambda amount=default_database_size: make_many(factory_registration, amount)


@pytest.fixture(name="create_registration_dto")
def create_registration_dto_fixture(factory_registration_create):
    return factory_registration_create()


@pytest.fixture(name="create_many_registrations_dto")
def create_many_registrations_dto_fixture(
    factory_registration_create, default_database_size
):
    return lambda amount=default_database_size: make_many(
        factory_registration_create, amount
    )


@pytest.fixture(name="default_database_size")
def default_database_size_fixture():
    return 10


@pytest.fixture(name="fill_database")
def fill_database_fixture(
    registrations: Callable[[int], List[Registration]], default_database_size: int
) -> Callable[[FakeDatabase], FakeDatabase]:
    regs = registrations

    def get_db(db: FakeDatabase):
        registrations_ = regs(default_database_size)
        drawings = [r.drawing for r in registrations_]

        db.repositories["Drawing"].session.data["Drawing"] = drawings
        db.repositories["Registration"].session.data["Registration"] = registrations_

        db.repositories["Drawing"]._pk_count = max(d.id for d in drawings) + 1
        db.repositories["Registration"]._pk_count = (
            max(r.id for r in registrations_) + 1
        )

        return db

    return get_db
