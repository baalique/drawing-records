import pytest

from app.domain.services.drawing import delete_drawing


@pytest.mark.unit
def test_delete_drawing(delete_function):
    id = 1
    delete_function.return_value = True

    result = delete_drawing(delete_function, id)

    delete_function.assert_called_once_with(id)
    assert result
