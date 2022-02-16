import pytest

from adapters.repository.fake.drawing import FakeSession, FakeDrawingRepository


@pytest.fixture(name="drawing_repository_empty")
def drawing_repository_empty_fixture() -> FakeDrawingRepository:
    session = FakeSession()
    repository = FakeDrawingRepository(session)
    return repository


@pytest.fixture(name="drawing_repository")
async def drawing_repository_fixture(create_many_drawing_dto) -> FakeDrawingRepository:
    session = FakeSession()
    repository = FakeDrawingRepository(session)
    for drawing in create_many_drawing_dto():
        await repository.add(drawing)
    return repository
