from copy import deepcopy
from datetime import datetime
from typing import Dict, Any

import pytest
from pydantic import ValidationError

from app.domain.entities.drawing import Drawing
from app.domain.entities.registration import Registration
from tests.unit.domain.entities.drawing.test_drawing import valid_drawing_dict_fixture


@pytest.fixture(name="valid_registration_dict")
def valid_registration_dict_fixture(valid_drawing_dict) -> Dict[str, Any]:
    _ = valid_drawing_dict_fixture
    return {
        "id": 1,
        "drawing": Drawing(**valid_drawing_dict),
        "created_at": datetime(year=2022, month=1, day=1, hour=1)
    }


@pytest.fixture(name="invalid_registration_dict")
def invalid_registration_dict_fixture() -> Dict[str, Any]:
    return {
        "id": "test id",
        "drawing": 1,
        "created_at": "test created_at"
    }


@pytest.mark.unit
class TestRegistration:
    class TestModel:
        def test_valid_registration(self, valid_registration_dict):
            assert Registration(**valid_registration_dict)

        def test_invalid_registration(self, invalid_registration_dict):
            with pytest.raises(ValidationError):
                Registration(**invalid_registration_dict)

        def test_is_required_attribute(self, valid_registration_dict):
            for attr in ("id", "drawing", "created_at"):
                copy_registration_dict = deepcopy(valid_registration_dict)
                copy_registration_dict.pop(attr)
                with pytest.raises(ValidationError):
                    Registration(**copy_registration_dict)

        def test_set_invalid_attributes(self, valid_registration_dict, invalid_registration_dict):
            registration = Registration(**valid_registration_dict)
            for attr in ("id", "drawing", "created_at"):
                with pytest.raises(ValidationError):
                    setattr(registration, attr, invalid_registration_dict[attr])
