from copy import deepcopy
from datetime import datetime
from typing import Dict, Any

import pytest
from pydantic import ValidationError

from app.domain.entities.registration import RegistrationCreate


@pytest.fixture(name="valid_registration_dict")
def valid_registration_dict_fixture() -> Dict[str, Any]:
    return {
        "drawing_id": 1,
        "created_at": datetime(year=2022, month=1, day=1, hour=1)
    }


@pytest.fixture(name="invalid_registration_dict")
def invalid_registration_dict_fixture() -> Dict[str, Any]:
    return {
        "drawing_id": "test id",
        "created_at": "test created_at"
    }


@pytest.mark.unit
class TestRegistrationCreate:
    class TestModel:
        def test_valid_registration(self, valid_registration_dict):
            assert RegistrationCreate(**valid_registration_dict)

        def test_invalid_registration(self, invalid_registration_dict):
            with pytest.raises(ValidationError):
                RegistrationCreate(**invalid_registration_dict)

        def test_is_required_attribute(self, valid_registration_dict):
            for attr in ("drawing_id", "created_at"):
                copy_registration_dict = deepcopy(valid_registration_dict)
                copy_registration_dict.pop(attr)
                with pytest.raises(ValidationError):
                    RegistrationCreate(**copy_registration_dict)
