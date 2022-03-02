import pytest
from pytest_factoryboy import register

from tests.factories.dtos.drawing import (
    FactoryDrawingDtoCreate,
    FactoryDrawingDtoOut,
    FactoryDrawingDtoUpdate,
)
from tests.factories.dtos.registration import (
    FactoryRegistrationDtoCreate,
    FactoryRegistrationDtoOut,
)
from tests.factories.entities.drawing import FactoryDrawing
from tests.fake.repositories import FakeDatabase
from tests.utils import make_many

for factory in (
    FactoryDrawing,
    FactoryDrawingDtoCreate,
    FactoryDrawingDtoOut,
    FactoryDrawingDtoUpdate,
    FactoryRegistrationDtoCreate,
    FactoryRegistrationDtoOut,
):
    register(factory)


@pytest.fixture(name="drawing")
def drawing_fixture(factory_drawing):
    return factory_drawing()


@pytest.fixture(name="drawings")
def drawings_fixture(factory_drawing, default_database_size):
    return lambda amount=default_database_size: make_many(factory_drawing, amount)


@pytest.fixture(name="drawing_dto_out")
def drawing_dto_out_fixture(factory_drawing_dto_out):
    return factory_drawing_dto_out()


@pytest.fixture(name="drawings_dto_out")
def drawings_dto_out_fixture(factory_drawing_dto_out, default_database_size):
    return lambda amount=default_database_size: make_many(
        factory_drawing_dto_out, amount
    )


@pytest.fixture(name="drawing_dto_create")
def drawing_dto_create_fixture(factory_drawing_dto_create):
    return factory_drawing_dto_create()


@pytest.fixture(name="drawings_dto_create")
def drawings_dto_create_fixture(factory_drawing_dto_create, default_database_size):
    return lambda amount=default_database_size: make_many(
        factory_drawing_dto_create, amount
    )


@pytest.fixture(name="drawing_dto_update")
def drawing_dto_update_fixture(factory_drawing_dto_update):
    return factory_drawing_dto_update()


@pytest.fixture(name="registration_dto_out")
def registration_dto_out_fixture(factory_registration_dto_out):
    return factory_registration_dto_out()


@pytest.fixture(name="registrations_dto_out")
def registrations_dto_out_fixture(factory_registration_dto_out, default_database_size):
    return lambda amount=default_database_size: make_many(
        factory_registration_dto_out, amount
    )


@pytest.fixture(name="registration_dto_create")
def registration_dto_create_fixture(factory_registration_dto_create):
    return factory_registration_dto_create()


@pytest.fixture(name="registrations_dto_create")
def registrations_dto_create_fixture(
    factory_registration_dto_create, default_database_size
):
    return lambda amount=default_database_size: make_many(
        factory_registration_dto_create, amount
    )


@pytest.fixture(name="default_database_size")
def default_database_size_fixture():
    return 10


@pytest.fixture(name="fill_database")
def fill_database_fixture(registrations, default_database_size: int):
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
