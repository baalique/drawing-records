import pytest

from adapters.repository.fake.drawing import FakeDrawingRepository
from db import get_db


@pytest.fixture(name="drawing_repository_empty")
def drawing_repository_empty_fixture() -> FakeDrawingRepository:
    return get_db().repositories["Drawing"]


@pytest.fixture(name="drawing_repository")
async def drawing_repository_fixture(create_many_drawing_dto) -> FakeDrawingRepository:
    repository = get_db().repositories["Drawing"]
    for drawing in create_many_drawing_dto():
        await repository.add(drawing)
    return repository
