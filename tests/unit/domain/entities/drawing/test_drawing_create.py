from copy import deepcopy
from typing import Dict, Any

import pytest
from pydantic import ValidationError

from app.domain.entities.drawing import DrawingCreate


@pytest.fixture(name="valid_drawing_dict")
def valid_drawing_dict_fixture() -> Dict[str, Any]:
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


@pytest.fixture(name="invalid_drawing_dict")
def invalid_drawing_dict_fixture() -> Dict[str, Any]:
    return {
        "name": [1],
        "parent_id": "test parent_id",
        "category": [1],
        "project": [1],
        "drawing_data": 1,
        "path_to_file": 1
    }


@pytest.mark.unit
class TestDrawingCreate:
    class TestModel:
        def test_valid_drawing(self, valid_drawing_dict):
            assert DrawingCreate(**valid_drawing_dict)

        def test_invalid_drawing(self, invalid_drawing_dict):
            with pytest.raises(ValidationError):
                DrawingCreate(**invalid_drawing_dict)

        def test_is_required_attributes(self, valid_drawing_dict):
            for attr in ("name", "category", "project", "drawing_data", "path_to_file"):
                copy_drawing_dict = deepcopy(valid_drawing_dict)
                copy_drawing_dict.pop(attr)
                with pytest.raises(ValidationError):
                    DrawingCreate(**copy_drawing_dict)

        def test_optional_attributes_are_not_required(self, valid_drawing_dict):
            valid_drawing_dict.pop("parent_id")
            assert DrawingCreate(**valid_drawing_dict)
