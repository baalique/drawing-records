from copy import deepcopy

import pytest
from pydantic import ValidationError

from app.domain.entities.registration import Registration


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
