import pytest

from app.service_layer.dtos.drawing import DrawingDtoOut, DrawingDtoUpdate
from app.service_layer.exceptions import AlreadyExistsError, NotFoundError
from app.service_layer.services.drawing import (
    create_drawing,
    delete_drawing,
    get_all_drawings,
    get_drawing_by_id,
    id_exists,
    update_drawing,
)


@pytest.mark.unit
@pytest.mark.asyncio
async def test_create_drawing_success(
    drawing_dto_create, fake_drawing_repository_empty
):
    result = await create_drawing(drawing_dto_create, fake_drawing_repository_empty)

    assert result == DrawingDtoOut(**drawing_dto_create.dict())


@pytest.mark.unit
@pytest.mark.asyncio
async def test_create_drawing_success_parent_exists(
    drawing_dto_create, fake_drawing_repository
):
    drawing = drawing_dto_create
    drawing.parent_id = fake_drawing_repository.data[0].id

    result = await create_drawing(drawing_dto_create, fake_drawing_repository)

    assert result == DrawingDtoOut(**drawing.dict())


@pytest.mark.unit
@pytest.mark.asyncio
async def test_create_drawing_fails_already_exists(
    drawing_dto_create, fake_drawing_repository
):
    drawing = drawing_dto_create
    drawing.id = fake_drawing_repository.data[0].id

    with pytest.raises(AlreadyExistsError):
        await create_drawing(drawing_dto_create, fake_drawing_repository)


@pytest.mark.unit
@pytest.mark.asyncio
async def test_create_drawing_fails_parent_not_exists(
    drawing_dto_create, fake_drawing_repository
):
    drawing = drawing_dto_create
    drawing.parent_id = max(d.id for d in fake_drawing_repository.data) + 1

    with pytest.raises(NotFoundError):
        await create_drawing(drawing_dto_create, fake_drawing_repository)


@pytest.mark.unit
@pytest.mark.asyncio
async def test_get_drawing_by_id_success(fake_drawing_repository):
    id_ = fake_drawing_repository.data[0].id

    result = await get_drawing_by_id(id_, fake_drawing_repository)

    assert result == DrawingDtoOut.from_entity(fake_drawing_repository.data[0])


@pytest.mark.unit
@pytest.mark.asyncio
async def test_get_drawing_by_id_fails_not_found(fake_drawing_repository_empty):
    with pytest.raises(NotFoundError):
        await get_drawing_by_id(1, fake_drawing_repository_empty)


@pytest.mark.unit
@pytest.mark.asyncio
async def test_get_all_drawings(fake_drawing_repository):
    result = await get_all_drawings(fake_drawing_repository)

    assert len(result) == len(fake_drawing_repository.data)


@pytest.mark.unit
@pytest.mark.asyncio
async def test_update_drawing_success(drawing_dto_update, fake_drawing_repository):
    drawing = drawing_dto_update
    drawing.id = max(d.id for d in fake_drawing_repository.data) + 1
    drawing.parent_id = None
    id_ = fake_drawing_repository.data[0].id

    result = await update_drawing(id_, drawing, fake_drawing_repository)

    assert result.dict().items() >= drawing.dict().items()
    assert result.parent_id is None


@pytest.mark.unit
@pytest.mark.asyncio
async def test_update_drawing_one_row_success(fake_drawing_repository):
    drawing = DrawingDtoUpdate(name="name", parent_id=None)
    id_ = fake_drawing_repository.data[0].id

    result = await update_drawing(id_, drawing, fake_drawing_repository)

    assert result.name == "name"


@pytest.mark.unit
@pytest.mark.asyncio
async def test_update_drawing_fails_no_such_id(
    drawing_dto_update, fake_drawing_repository
):
    id_ = max(d.id for d in fake_drawing_repository.data) + 1

    with pytest.raises(NotFoundError):
        await update_drawing(id_, drawing_dto_update, fake_drawing_repository)


@pytest.mark.unit
@pytest.mark.asyncio
async def test_update_drawing_fails_id_already_exists(
    drawing_dto_update, fake_drawing_repository
):
    drawing = drawing_dto_update
    drawing.id = fake_drawing_repository.data[0].id
    id_ = fake_drawing_repository.data[1].id

    with pytest.raises(AlreadyExistsError):
        await update_drawing(id_, drawing, fake_drawing_repository)


@pytest.mark.unit
@pytest.mark.asyncio
async def test_update_drawing_fails_no_such_parent_id(
    drawing_dto_update, fake_drawing_repository
):
    drawing = drawing_dto_update
    drawing.parent_id = max(d.id for d in fake_drawing_repository.data) + 1
    id_ = fake_drawing_repository.data[1].id

    with pytest.raises(NotFoundError):
        await update_drawing(id_, drawing, fake_drawing_repository)


@pytest.mark.unit
@pytest.mark.asyncio
async def test_delete_drawing_success(fake_drawing_repository):
    id_ = fake_drawing_repository.data[0].id
    len_ = len(fake_drawing_repository.data)

    result = await delete_drawing(id_, fake_drawing_repository)

    assert result is True
    assert len(fake_drawing_repository.data) == len_ - 1
    assert not list(filter(lambda d: d.id == id_, fake_drawing_repository.data))


@pytest.mark.unit
@pytest.mark.asyncio
async def test_delete_drawing_fails_not_found(fake_drawing_repository):
    id_ = max(d.id for d in fake_drawing_repository.data) + 1

    with pytest.raises(NotFoundError):
        await delete_drawing(id_, fake_drawing_repository)


@pytest.mark.unit
@pytest.mark.asyncio
async def test_drawing_id_exists(fake_drawing_repository):
    id_ = fake_drawing_repository.data[0].id

    result = await id_exists(id_, fake_drawing_repository)

    assert result is True


@pytest.mark.unit
@pytest.mark.asyncio
async def test_drawing_id_not_exists(fake_drawing_repository):
    id_ = max(d.id for d in fake_drawing_repository.data) + 1

    result = await id_exists(id_, fake_drawing_repository)

    assert result is False
