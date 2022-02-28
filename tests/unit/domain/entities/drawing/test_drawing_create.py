from copy import deepcopy

import pytest
from pydantic import ValidationError

from app.service_layer.dtos.drawing import DrawingDtoCreate


@pytest.mark.unit
class TestDrawingCreate:
    class TestModel:
        def test_valid_drawing(self, valid_drawing_create_dict):
            assert DrawingDtoCreate(**valid_drawing_create_dict)

        def test_invalid_drawing(self, invalid_drawing_create_dict):
            with pytest.raises(ValidationError):
                DrawingDtoCreate(**invalid_drawing_create_dict)

        def test_is_required_attributes(self, valid_drawing_create_dict):
            for attr in ("name", "category", "project", "drawing_data", "path_to_file"):
                copy_drawing_dict = deepcopy(valid_drawing_create_dict)
                copy_drawing_dict.pop(attr)
                with pytest.raises(ValidationError):
                    DrawingDtoCreate(**copy_drawing_dict)

        def test_optional_attributes_are_not_required(self, valid_drawing_create_dict):
            valid_drawing_create_dict.pop("parent_id")
            assert DrawingDtoCreate(**valid_drawing_create_dict)
