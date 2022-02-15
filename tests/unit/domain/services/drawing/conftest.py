import pytest
from pytest_factoryboy import register

from tests.factories.entities.drawing import FactoryDrawing, FactoryDrawingCreate, FactoryDrawingUpdate
from tests.utils import make_many

for factory in (FactoryDrawing, FactoryDrawingCreate, FactoryDrawingUpdate):
    register(factory)


@pytest.fixture(name="create_function")
def create_function_fixture(mocker):
    return mocker.stub(name="create_function")


@pytest.fixture(name="get_by_id_function")
def get_by_id_function_fixture(mocker):
    return mocker.stub(name="get_by_id_function")


@pytest.fixture(name="get_all_function")
def get_all_function_fixture(mocker):
    return mocker.stub(name="get_all_function")


@pytest.fixture(name="update_function")
def update_function_fixture(mocker):
    return mocker.stub(name="update_function")


@pytest.fixture(name="delete_function")
def delete_function_fixture(mocker):
    return mocker.stub(name="delete_function")


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
