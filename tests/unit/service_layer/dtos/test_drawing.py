from copy import deepcopy

import pytest
from pydantic import ValidationError

from app.service_layer.dtos.drawing import (
    DrawingDtoCreate,
    DrawingDtoOut,
    DrawingDtoUpdate,
)


@pytest.mark.unit
class TestDrawingDtoCreate:
    def test_valid_drawing(self, valid_drawing_dto_create_dict):
        assert DrawingDtoCreate(**valid_drawing_dto_create_dict)

    def test_invalid_drawing(self, invalid_drawing_dto_create_dict):
        with pytest.raises(ValidationError):
            DrawingDtoCreate(**invalid_drawing_dto_create_dict)

    def test_is_required_attributes(self, valid_drawing_dto_create_dict):
        for attr in (
            "id",
            "name",
            "category",
            "project",
            "drawing_data",
            "path_to_file",
        ):
            copy_drawing_dict = deepcopy(valid_drawing_dto_create_dict)
            copy_drawing_dict.pop(attr)
            with pytest.raises(ValidationError):
                DrawingDtoCreate(**copy_drawing_dict)


@pytest.mark.unit
class TestDrawingDtoUpdate:
    def test_valid_drawing(self, valid_drawing_dto_update_dict):
        assert DrawingDtoUpdate(**valid_drawing_dto_update_dict)

    def test_invalid_drawing(self, invalid_drawing_dto_update_dict):
        with pytest.raises(ValidationError):
            DrawingDtoUpdate(**invalid_drawing_dto_update_dict)

    def test_optional_attributes_are_not_required(self, valid_drawing_dto_update_dict):
        for attr in (
            "name",
            "category",
            "project",
            "drawing_data",
            "path_to_file",
        ):
            copy_drawing_dict = deepcopy(valid_drawing_dto_update_dict)
            copy_drawing_dict.pop(attr)
            assert DrawingDtoUpdate(**copy_drawing_dict)


@pytest.mark.unit
class TestDrawingDtoOut:
    def test_valid_drawing(self, valid_drawing_dto_out_dict):
        assert DrawingDtoOut(**valid_drawing_dto_out_dict)

    def test_invalid_drawing(self, invalid_drawing_dto_out_dict):
        with pytest.raises(ValidationError):
            DrawingDtoOut(**invalid_drawing_dto_out_dict)

    def test_is_required_attribute(self, valid_drawing_dto_out_dict):
        for attr in (
            "id",
            "name",
            "category",
            "project",
            "drawing_data",
            "path_to_file",
        ):
            copy_drawing_dict = deepcopy(valid_drawing_dto_out_dict)
            copy_drawing_dict.pop(attr)
            with pytest.raises(ValidationError):
                DrawingDtoOut(**copy_drawing_dict)

    def test_set_invalid_attributes(
        self, valid_drawing_dto_out_dict, invalid_drawing_dto_out_dict
    ):
        drawing = DrawingDtoOut(**valid_drawing_dto_out_dict)
        for attr in (
            "id",
            "name",
            "parent_id",
            "category",
            "project",
            "drawing_data",
            "path_to_file",
        ):
            with pytest.raises(ValidationError):
                setattr(drawing, attr, invalid_drawing_dto_out_dict[attr])
