import pytest

from app.domain.services.drawing import create_drawing


@pytest.mark.unit
@pytest.mark.asyncio
async def test_create_drawing(create_function, create_drawing_dto, drawing):
    create_function.return_value.set_result(drawing)

    result = await create_drawing(create_function, create_drawing_dto)

    create_function.assert_called_once_with(create_drawing_dto)
    assert result == drawing
