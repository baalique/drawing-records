import pytest

from app.domain.services.drawing import get_drawing_by_id, get_all_drawings


@pytest.mark.unit
def test_get_drawing_by_id(get_by_id_function, drawing):
    id = drawing.id
    get_by_id_function.return_value = drawing

    result = get_drawing_by_id(get_by_id_function, id)

    get_by_id_function.assert_called_once_with(id)
    assert result == drawing


@pytest.mark.unit
def test_get_all_drawings(get_all_function, drawings):
    drawings = drawings()
    get_all_function.return_value = drawings

    result = get_all_drawings(get_all_function)

    get_all_function.assert_called_once_with()
    assert result == drawings
