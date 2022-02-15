from typing import Dict, Any

import pytest


@pytest.fixture(name="invalid_drawing_dict")
def invalid_drawing_dict_fixture() -> Dict[str, Any]:
    return {
        "id": "test id",
        "name": [1],
        "parent": 1,
        "category": [1],
        "project": [1],
        "drawing_data": 1,
        "path_to_file": 1
    }


@pytest.fixture(name="valid_drawing_create_dict")
def valid_drawing_create_dict_fixture() -> Dict[str, Any]:
    return {
        "name": "test drawing",
        "parent_id": 1,
        "category": "test category",
        "project": "test project",
        "drawing_data": {
            "test_data": "test data"
        },
        "path_to_file": "/home/test/test.some"
    }


@pytest.fixture(name="invalid_drawing_create_dict")
def invalid_drawing_create_dict_fixture() -> Dict[str, Any]:
    return {
        "name": [1],
        "parent_id": "test parent_id",
        "category": [1],
        "project": [1],
        "drawing_data": 1,
        "path_to_file": 1
    }


@pytest.fixture(name="valid_drawing_update_dict")
def valid_drawing_update_dict_fixture() -> Dict[str, Any]:
    return {
        "name": "test drawing",
        "parent_id": 1,
        "category": "test category",
        "project": "test project",
        "drawing_data": {
            "test_data": "test data"
        },
        "path_to_file": "/home/test/test.some"
    }


@pytest.fixture(name="invalid_drawing_update_dict")
def invalid_drawing_update_dict_fixture() -> Dict[str, Any]:
    return {
        "name": [1],
        "parent_id": "test parent_id",
        "category": [1],
        "project": [1],
        "drawing_data": 1,
        "path_to_file": 1
    }
