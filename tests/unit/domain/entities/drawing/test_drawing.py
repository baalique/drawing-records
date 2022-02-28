from copy import deepcopy

import pytest
from pydantic import ValidationError

from app.service_layer.dtos.drawing import DrawingDtoOut


@pytest.mark.unit
class TestDrawing:
    class TestModel:
        def test_valid_drawing(self, valid_drawing_dict):
            assert DrawingDtoOut(**valid_drawing_dict)

        def test_invalid_drawing(self, invalid_drawing_dict):
            with pytest.raises(ValidationError):
                DrawingDtoOut(**invalid_drawing_dict)

        def test_is_required_attribute(self, valid_drawing_dict):
            for attr in (
                "id",
                "name",
                "category",
                "project",
                "drawing_data",
                "path_to_file",
            ):
                copy_drawing_dict = deepcopy(valid_drawing_dict)
                copy_drawing_dict.pop(attr)
                with pytest.raises(ValidationError):
                    DrawingDtoOut(**copy_drawing_dict)

        def test_optional_attributes_are_not_required(self, valid_drawing_dict):
            valid_drawing_dict.pop("parent")
            assert DrawingDtoOut(**valid_drawing_dict)

        def test_set_invalid_attributes(self, valid_drawing_dict, invalid_drawing_dict):
            drawing = DrawingDtoOut(**valid_drawing_dict)
            for attr in (
                "id",
                "name",
                "parent",
                "category",
                "project",
                "drawing_data",
                "path_to_file",
            ):
                with pytest.raises(ValidationError):
                    setattr(drawing, attr, invalid_drawing_dict[attr])

        def test_parent_can_be_drawing(self, valid_drawing_dict):
            drawing = DrawingDtoOut(**valid_drawing_dict)
            parent_drawing = DrawingDtoOut(**(valid_drawing_dict | {"id": 2}))
            drawing.parent = parent_drawing
