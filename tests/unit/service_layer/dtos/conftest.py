from datetime import datetime
from typing import Any, Dict

import pytest
from service_layer.dtos.drawing import DrawingDtoOut


@pytest.fixture(name="valid_drawing_dto_out_dict")
def valid_drawing_dto_out_dict_fixture() -> Dict[str, Any]:
    return {
        "id": 1,
        "name": "test drawing",
        "parent_id": None,
        "category": "test category",
        "project": "test project",
        "drawing_data": {"test_data": "test data"},
        "path_to_file": "/home/test/test.some",
    }


@pytest.fixture(name="invalid_drawing_dto_out_dict")
def invalid_drawing_dto_out_dict_fixture() -> Dict[str, Any]:
    return {
        "id": "test id",
        "name": [1],
        "parent_id": "test parent_id",
        "category": [1],
        "project": [1],
        "drawing_data": 1,
        "path_to_file": 1,
    }


@pytest.fixture(name="valid_drawing_dto_create_dict")
def valid_drawing_dto_create_dict_fixture() -> Dict[str, Any]:
    return {
        "id": 1,
        "name": "test drawing",
        "parent_id": 1,
        "category": "test category",
        "project": "test project",
        "drawing_data": {"test_data": "test data"},
        "path_to_file": "/home/test/test.some",
    }


@pytest.fixture(name="invalid_drawing_dto_create_dict")
def invalid_drawing_dto_create_dict_fixture() -> Dict[str, Any]:
    return {
        "id": "test id",
        "name": [1],
        "parent_id": "test parent_id",
        "category": [1],
        "project": [1],
        "drawing_data": 1,
        "path_to_file": 1,
    }


@pytest.fixture(name="valid_drawing_dto_update_dict")
def valid_drawing_dto_update_dict_fixture() -> Dict[str, Any]:
    return {
        "id": 1,
        "name": "test drawing",
        "parent_id": 1,
        "category": "test category",
        "project": "test project",
        "drawing_data": {"test_data": "test data"},
        "path_to_file": "/home/test/test.some",
    }


@pytest.fixture(name="invalid_drawing_dto_update_dict")
def invalid_drawing_dto_update_dict_fixture() -> Dict[str, Any]:
    return {
        "name": [1],
        "parent_id": "test parent_id",
        "category": [1],
        "project": [1],
        "drawing_data": 1,
        "path_to_file": 1,
    }


@pytest.fixture(name="valid_registration_dto_out_dict")
def valid_registration_dto_out_dict_fixture(valid_drawing_dict) -> Dict[str, Any]:
    return {
        "id": 1,
        "drawing": DrawingDtoOut(**valid_drawing_dict),
        "created_at": datetime(year=2022, month=1, day=1, hour=1),
    }


@pytest.fixture(name="invalid_registration_dto_out_dict")
def invalid_registration_dto_out_dict_fixture() -> Dict[str, Any]:
    return {"id": "test id", "drawing": 1, "created_at": "test created_at"}


@pytest.fixture(name="valid_registration_dto_create_dict")
def valid_registration_create_dto_dict_fixture() -> Dict[str, Any]:
    return {"drawing_id": 1, "created_at": datetime(year=2022, month=1, day=1, hour=1)}


@pytest.fixture(name="invalid_registration_dto_create_dict")
def invalid_registration_dto_create_dict_fixture() -> Dict[str, Any]:
    return {"drawing_id": "test id", "created_at": "test created_at"}
