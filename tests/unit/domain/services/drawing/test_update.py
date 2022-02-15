import pytest

from app.domain.services.drawing import update_drawing


@pytest.mark.unit
@pytest.mark.asyncio
async def test_update_drawing(update_function, update_drawing_dto, drawing):
    id = 1
    update_function.return_value.set_result(drawing)

    result = await update_drawing(update_function, update_drawing_dto, id)

    update_function.assert_called_once_with(update_drawing_dto, id)
    assert result == drawing
