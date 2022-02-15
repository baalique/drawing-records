import pytest
from pytest_factoryboy import register

from tests.factories.entities.registration import FactoryRegistration, FactoryRegistrationCreate
from tests.utils import make_many

for factory in (FactoryRegistration, FactoryRegistrationCreate):
    register(factory)


@pytest.fixture(name="create_registration_dto")
def create_registration_dto_fixture(factory_registration_create):
    return factory_registration_create()


@pytest.fixture(name="registration")
def registration(factory_registration):
    return factory_registration()


@pytest.fixture(name="registrations")
def registrations(factory_registration):
    return lambda amount=10: make_many(factory_registration, amount)
