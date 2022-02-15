import pytest
from pytest_factoryboy import register

from tests.factories.entities.drawing import FactoryDrawing, FactoryDrawingCreate, FactoryDrawingUpdate
from tests.utils import make_many

for factory in (FactoryDrawing, FactoryDrawingCreate, FactoryDrawingUpdate):
    register(factory)


@pytest.fixture(name="create_drawing_dto")
def create_drawing_dto_fixture(factory_drawing_create):
    return factory_drawing_create()


@pytest.fixture(name="drawing")
def drawing(factory_drawing):
    return factory_drawing()


@pytest.fixture(name="drawings")
def drawings(factory_drawing):
    return lambda amount=10: make_many(factory_drawing, amount)


@pytest.fixture(name="update_drawing_dto")
def update_drawing_dto_fixture(factory_drawing_update):
    return factory_drawing_update()
