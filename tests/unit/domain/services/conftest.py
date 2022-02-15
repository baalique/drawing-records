import pytest


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
