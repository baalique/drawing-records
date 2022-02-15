import pytest

from app.domain.services.registration import delete_registration


@pytest.mark.unit
@pytest.mark.asyncio
async def test_delete_registration(delete_function):
    id = 1
    delete_function.return_value.set_result(True)

    result = await delete_registration(delete_function, id)

    delete_function.assert_called_once_with(id)
    assert result is True
