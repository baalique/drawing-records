import pytest


@pytest.mark.unit
@pytest.mark.asyncio
async def test_initial_repository_empty(drawing_repository_empty):
    result = await drawing_repository_empty.list()

    assert result == []


@pytest.mark.unit
@pytest.mark.asyncio
async def test_add_one_drawing(drawing_repository, drawing):
    drawings = await drawing_repository.list()
    start_len = len(drawings)

    drawing.id = max(d.id for d in drawings) + 1
    drawing.parent_id = None

    await drawing_repository.add(drawing)
    result = await drawing_repository.list()

    assert len(result) == start_len + 1
    assert drawing.id in [d.id for d in result]


@pytest.mark.unit
@pytest.mark.asyncio
async def test_get_one_drawing(drawing_repository, drawing):
    drawings = await drawing_repository.list()
    drawing.id = max(d.id for d in drawings) + 1
    drawing = await drawing_repository.add(drawing)
    id_ = drawing.id

    result = await drawing_repository.get(id_)

    assert result == drawing


@pytest.mark.unit
@pytest.mark.asyncio
async def test_get_one_drawing_fails_no_such_id(drawing_repository_empty):
    result = await drawing_repository_empty.get(1)

    assert result is None


@pytest.mark.unit
@pytest.mark.asyncio
async def test_get_all_drawings(drawing_repository_empty, drawings):
    drawings = drawings()
    for drawing in drawings:
        await drawing_repository_empty.add(drawing)

    result = await drawing_repository_empty.list()

    assert len(result) == len(drawings)
    assert {d.id for d in result} == {d.id for d in drawings}


@pytest.mark.unit
@pytest.mark.asyncio
async def test_update_drawing(drawing_repository, drawing_dto_update):
    drawings = await drawing_repository.list()
    id_ = drawings[0].id
    del drawing_dto_update.id

    await drawing_repository.update(id_, drawing_dto_update.dict())

    result = await drawing_repository.get(id_)

    assert result.name == drawing_dto_update.name


@pytest.mark.unit
@pytest.mark.asyncio
async def test_update_drawing_fails_no_such_id(
        drawing_repository_empty, drawing_dto_update
):
    result = await drawing_repository_empty.update(1, drawing_dto_update.dict())

    assert result is None


@pytest.mark.unit
@pytest.mark.asyncio
async def test_delete_drawing(drawing_repository):
    drawings = await drawing_repository.list()
    id_ = drawings[0].id
    start_len = len(drawings)

    result = await drawing_repository.delete(id_)
    new_drawings = await drawing_repository.list()
    deleted_drawing = await drawing_repository.get(id_)

    assert result is True
    assert len(new_drawings) == start_len - 1
    assert deleted_drawing is None


@pytest.mark.unit
@pytest.mark.asyncio
async def test_delete_drawing_fails_no_such_id(drawing_repository_empty):
    res = await drawing_repository_empty.list()
    result = await drawing_repository_empty.delete(1)

    assert result is False
