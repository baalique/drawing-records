from copy import deepcopy

import pytest
from pydantic import ValidationError

from app.service_layer.dtos.registration import (
    RegistrationDtoCreate,
    RegistrationDtoOut,
)


@pytest.mark.unit
class TestRegistrationDtoOut:
    def test_valid_registration(self, valid_registration_dto_out_dict):
        assert RegistrationDtoOut(**valid_registration_dto_out_dict)

    def test_invalid_registration(self, invalid_registration_dto_out_dict):
        with pytest.raises(ValidationError):
            RegistrationDtoOut(**invalid_registration_dto_out_dict)

    def test_is_required_attribute(self, valid_registration_dto_out_dict):
        for attr in ("id", "drawing", "created_at"):
            copy_registration_dict = deepcopy(valid_registration_dto_out_dict)
            copy_registration_dict.pop(attr)
            with pytest.raises(ValidationError):
                RegistrationDtoOut(**copy_registration_dict)

    def test_set_invalid_attributes(
        self, valid_registration_dto_out_dict, invalid_registration_dto_out_dict
    ):
        registration = RegistrationDtoOut(**valid_registration_dto_out_dict)
        for attr in ("id", "drawing", "created_at"):
            with pytest.raises(ValidationError):
                setattr(registration, attr, invalid_registration_dto_out_dict[attr])


@pytest.mark.unit
class TestRegistrationDtoCreate:
    def test_valid_registration(self, valid_registration_dto_create_dict):
        assert RegistrationDtoCreate(**valid_registration_dto_create_dict)

    def test_invalid_registration(self, invalid_registration_dto_create_dict):
        with pytest.raises(ValidationError):
            RegistrationDtoCreate(**invalid_registration_dto_create_dict)

    def test_is_required_attribute(self, valid_registration_dto_create_dict):
        for attr in ("drawing_id", "created_at"):
            copy_registration_dict = deepcopy(valid_registration_dto_create_dict)
            copy_registration_dict.pop(attr)
            with pytest.raises(ValidationError):
                RegistrationDtoCreate(**copy_registration_dict)
