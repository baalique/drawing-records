import pytest

from app.domain.services.registration import create_registration


@pytest.mark.unit
def test_create_registration(create_function, create_registration_dto, registration):
    create_function.return_value = registration

    result = create_registration(create_function, create_registration_dto)

    create_function.assert_called_once_with(create_registration_dto)
    assert result == registration
