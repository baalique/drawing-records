from asyncio import Future

import pytest


@pytest.fixture(name="create_function")
def create_function_fixture(mocker):
    return mocker.MagicMock(name="create_function", return_value=Future())


@pytest.fixture(name="get_by_id_function")
def get_by_id_function_fixture(mocker):
    return mocker.MagicMock(name="get_by_id_function", return_value=Future())


@pytest.fixture(name="get_all_function")
def get_all_function_fixture(mocker):
    return mocker.MagicMock(name="get_all_function", return_value=Future())


@pytest.fixture(name="update_function")
def update_function_fixture(mocker):
    return mocker.MagicMock(name="update_function", return_value=Future())


@pytest.fixture(name="delete_function")
def delete_function_fixture(mocker):
    return mocker.MagicMock(name="delete_function", return_value=Future())
