from copy import deepcopy

import pytest
from pydantic import ValidationError

from app.domain.entities.registration import RegistrationCreate


@pytest.mark.unit
class TestRegistrationCreate:
    class TestModel:
        def test_valid_registration(self, valid_registration_create_dict):
            assert RegistrationCreate(**valid_registration_create_dict)

        def test_invalid_registration(self, invalid_registration_create_dict):
            with pytest.raises(ValidationError):
                RegistrationCreate(**invalid_registration_create_dict)

        def test_is_required_attribute(self, valid_registration_create_dict):
            for attr in ("drawing_id", "created_at"):
                copy_registration_dict = deepcopy(valid_registration_create_dict)
                copy_registration_dict.pop(attr)
                with pytest.raises(ValidationError):
                    RegistrationCreate(**copy_registration_dict)
