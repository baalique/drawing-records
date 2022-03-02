import pytest

from tests.fake.repositories import FakeSession
from tests.fake.repositories.drawing import FakeDrawingRepository


@pytest.fixture(name="fake_drawing_repository_empty")
def fake_drawing_repository_empty_fixture():
    session = FakeSession()
    repo = FakeDrawingRepository(session)
    return repo


@pytest.fixture(name="fake_drawing_repository")
def fake_drawing_repository_fixture(drawings):
    drawings = drawings()
    drawings[0].parent_id = drawings[1].id
    session = FakeSession()
    repo = FakeDrawingRepository(session)
    session.data = {"Drawing": drawings}
    return repo
