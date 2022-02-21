import pytest
from pytest_factoryboy import register

from tests.factories.entities.drawing import FactoryDrawing, FactoryDrawingCreate, FactoryDrawingUpdate
from tests.factories.entities.registration import FactoryRegistration, FactoryRegistrationCreate
from tests.utils import make_many

for factory in (
        FactoryDrawing,
        FactoryDrawingCreate,
        FactoryDrawingUpdate,
        FactoryRegistration,
        FactoryRegistrationCreate
):
    register(factory)


@pytest.fixture(name="drawing")
def drawing_fixture(factory_drawing):
    return factory_drawing()


@pytest.fixture(name="drawings")
def drawings_fixture(factory_drawing):
    return lambda amount=10: make_many(factory_drawing, amount)


@pytest.fixture(name="create_drawing_dto")
def create_drawing_dto_fixture(factory_drawing_create):
    return factory_drawing_create()


@pytest.fixture(name="create_many_drawings_dto")
def create_many_drawings_dto_fixture(factory_drawing_create):
    return lambda amount=10: make_many(factory_drawing_create, amount)


@pytest.fixture(name="update_drawing_dto")
def update_drawing_dto_fixture(factory_drawing_update):
    return factory_drawing_update()


@pytest.fixture(name="registration")
def registration_fixture(factory_registration):
    return factory_registration()


@pytest.fixture(name="registrations")
def registrations_fixture(factory_registration):
    return lambda amount=10: make_many(factory_registration, amount)


@pytest.fixture(name="create_registration_dto")
def create_registration_dto_fixture(factory_registration_create):
    return factory_registration_create()


@pytest.fixture(name="create_many_registrations_dto")
def create_many_registrations_dto_fixture(factory_registration_create):
    return lambda amount=10: make_many(factory_registration_create, amount)
