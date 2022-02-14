from copy import deepcopy
from typing import Dict, Any

import pytest
from pydantic import ValidationError

from app.domain.entities.drawing import Drawing


@pytest.fixture(name="valid_drawing_dict")
def valid_drawing_dict_fixture() -> Dict[str, Any]:
    return {
        "id": 1,
        "name": "test drawing",
        "parent": None,
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
        "id": "test id",
        "name": [1],
        "parent": 1,
        "category": [1],
        "project": [1],
        "drawing_data": 1,
        "path_to_file": 1
    }


@pytest.mark.unit
class TestDrawing:
    class TestModel:
        def test_valid_drawing(self, valid_drawing_dict):
            assert Drawing(**valid_drawing_dict)

        def test_invalid_drawing(self, invalid_drawing_dict):
            with pytest.raises(ValidationError):
                Drawing(**invalid_drawing_dict)

        def test_is_required_attribute(self, valid_drawing_dict):
            for attr in ("id", "name", "category", "project", "drawing_data", "path_to_file"):
                copy_drawing_dict = deepcopy(valid_drawing_dict)
                copy_drawing_dict.pop(attr)
                with pytest.raises(ValidationError):
                    Drawing(**copy_drawing_dict)

        def test_optional_attributes_are_not_required(self, valid_drawing_dict):
            valid_drawing_dict.pop("parent")
            assert Drawing(**valid_drawing_dict)

        def test_set_invalid_attributes(self, valid_drawing_dict, invalid_drawing_dict):
            drawing = Drawing(**valid_drawing_dict)
            for attr in ("id", "name", "parent", "category", "project", "drawing_data", "path_to_file"):
                with pytest.raises(ValidationError):
                    setattr(drawing, attr, invalid_drawing_dict[attr])

        def test_parent_can_be_drawing(self, valid_drawing_dict):
            drawing = Drawing(**valid_drawing_dict)
            parent_drawing = Drawing(**(valid_drawing_dict | {"id": 2}))
            setattr(drawing, "parent", parent_drawing)
