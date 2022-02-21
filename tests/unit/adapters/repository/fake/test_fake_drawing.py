from typing import List, Callable

import pytest

from adapters.repository.fake.drawing import FakeDrawingRepository
from domain.entities.drawing import DrawingCreate, DrawingUpdate


class TestFakeDrawingRepository:
    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_initial_repository_empty(self, drawing_repository_empty: FakeDrawingRepository):
        result = await drawing_repository_empty.list()
        assert result == []

    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_add_one_drawing(self, drawing_repository: FakeDrawingRepository,
                                   create_drawing_dto: DrawingCreate):
        drawings = await drawing_repository.list()
        start_len = len(drawings)

        await drawing_repository.add(create_drawing_dto)
        new_drawings = await drawing_repository.list()

        assert len(new_drawings) == start_len + 1

    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_add_one_drawing_increases_pk(self, drawing_repository: FakeDrawingRepository,
                                                create_drawing_dto: DrawingCreate):
        drawings = await drawing_repository.list()

        start_max_id = max(d.id for d in drawings)

        new_drawing = await drawing_repository.add(create_drawing_dto)

        assert new_drawing.id == start_max_id + 1

    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_add_one_drawing_fails_wrong_type(self, drawing_repository: FakeDrawingRepository):
        with pytest.raises(AttributeError):
            await drawing_repository.add("test data")

    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_get_one_drawing(self, drawing_repository: FakeDrawingRepository,
                                   create_drawing_dto: DrawingCreate):
        drawing = await drawing_repository.add(create_drawing_dto)
        id_ = drawing.id

        added_drawing = await drawing_repository.get(id_)

        assert drawing == added_drawing

    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_get_one_drawing_fails_no_such_id(self, drawing_repository: FakeDrawingRepository):
        drawings = await drawing_repository.list()
        max_id = max(d.id for d in drawings)

        result = await drawing_repository.get(max_id + 1)

        assert result is None

    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_get_all_drawings(self, drawing_repository_empty: FakeDrawingRepository,
                                    create_many_drawing_dto: Callable[[int], List[DrawingCreate]]):
        nb_of_drawings = 10

        drawings = create_many_drawing_dto(nb_of_drawings)
        for drawing in drawings:
            await drawing_repository_empty.add(drawing)

        created_drawings = await drawing_repository_empty.list()

        assert len(created_drawings) == nb_of_drawings

    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_update_drawing(self, drawing_repository: FakeDrawingRepository,
                                  update_drawing_dto: DrawingUpdate):
        drawings = await drawing_repository.list()
        id_ = drawings[0].id

        updated_drawing = await drawing_repository.update(update_drawing_dto, id_)

        new_drawing = await drawing_repository.get(id_)

        assert updated_drawing == new_drawing

    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_update_drawing_fails_no_such_id(self, drawing_repository: FakeDrawingRepository,
                                                   update_drawing_dto: DrawingUpdate):
        drawings = await drawing_repository.list()
        max_id = max(d.id for d in drawings)

        updated_drawing = await drawing_repository.update(update_drawing_dto, max_id + 1)

        assert updated_drawing is None

    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_update_drawing_fails_wrong_type(self, drawing_repository: FakeDrawingRepository):
        with pytest.raises(AttributeError):
            await drawing_repository.update("test data", 1)

    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_delete_drawing(self, drawing_repository: FakeDrawingRepository):
        drawings = await drawing_repository.list()
        id_ = drawings[0].id
        start_len = len(drawings)

        await drawing_repository.delete(id_)
        new_drawings = await drawing_repository.list()
        deleted_drawing = await drawing_repository.get(id_)

        assert len(new_drawings) == start_len - 1
        assert deleted_drawing is None

    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_delete_drawing_fails_no_such_id(self, drawing_repository: FakeDrawingRepository):
        drawings = await drawing_repository.list()
        max_id = max(d.id for d in drawings)
        start_len = len(drawings)

        was_drawing_deleted = await drawing_repository.delete(max_id + 1)
        new_drawings = await drawing_repository.list()

        assert not was_drawing_deleted
        assert start_len == len(new_drawings)

    @pytest.mark.unit
    def test_call_drawing_repository_returns_itself(self, drawing_repository: FakeDrawingRepository):
        assert drawing_repository == drawing_repository()

    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_truncate_database(self, drawing_repository: FakeDrawingRepository):
        await drawing_repository.clear()
        drawings = await drawing_repository.list()

        assert drawings == []
