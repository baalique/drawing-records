from copy import deepcopy

import pytest
from pydantic import ValidationError

from app.service_layer.dtos.drawing import DrawingDtoUpdate


@pytest.mark.unit
class TestDrawingUpdate:
    class TestModel:
        def test_valid_drawing(self, valid_drawing_update_dict):
            assert DrawingDtoUpdate(**valid_drawing_update_dict)

        def test_invalid_drawing(self, invalid_drawing_update_dict):
            with pytest.raises(ValidationError):
                DrawingDtoUpdate(**invalid_drawing_update_dict)

        def test_optional_attributes_are_not_required(self, valid_drawing_update_dict):
            for attr in (
                "name",
                "parent_id",
                "category",
                "project",
                "drawing_data",
                "path_to_file",
            ):
                copy_drawing_dict = deepcopy(valid_drawing_update_dict)
                copy_drawing_dict.pop(attr)
                assert DrawingDtoUpdate(**copy_drawing_dict)
