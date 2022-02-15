import pytest

from app.domain.services.registration import delete_registration


@pytest.mark.unit
def test_delete_registration(delete_function):
    id = 1
    delete_function.return_value = True

    result = delete_registration(delete_function, id)

    delete_function.assert_called_once_with(id)
    assert result
