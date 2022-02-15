import pytest

from app.domain.services.registration import get_registration_by_id, get_all_registrations


@pytest.mark.unit
def test_get_registration_by_id(get_by_id_function, registration):
    id = registration.id
    get_by_id_function.return_value = registration

    result = get_registration_by_id(get_by_id_function, id)

    get_by_id_function.assert_called_once_with(id)
    assert result == registration


@pytest.mark.unit
def test_get_all_registrations(get_all_function, registrations):
    registrations = registrations()
    get_all_function.return_value = registrations

    result = get_all_registrations(get_all_function)

    get_all_function.assert_called_once_with()
    assert result == registrations
