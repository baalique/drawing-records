from datetime import datetime
from typing import Any, Dict

import pytest

from app.domain.entities.drawing import Drawing


@pytest.fixture(name="valid_registration_dict")
def valid_registration_dict_fixture(valid_drawing_dict) -> Dict[str, Any]:
    return {
        "id": 1,
        "drawing": Drawing(**valid_drawing_dict),
        "created_at": datetime(year=2022, month=1, day=1, hour=1),
    }


@pytest.fixture(name="invalid_registration_dict")
def invalid_registration_dict_fixture() -> Dict[str, Any]:
    return {"id": "test id", "drawing": 1, "created_at": "test created_at"}


@pytest.fixture(name="valid_registration_create_dict")
def valid_registration_create_dict_fixture() -> Dict[str, Any]:
    return {"drawing_id": 1, "created_at": datetime(year=2022, month=1, day=1, hour=1)}


@pytest.fixture(name="invalid_registration_create_dict")
def invalid_registration_create_dict_fixture() -> Dict[str, Any]:
    return {"drawing_id": "test id", "created_at": "test created_at"}
