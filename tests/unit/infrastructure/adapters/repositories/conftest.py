import asyncio

import pytest

from app.infrastructure.adapters.repositories.drawing import SQLAlchemyDrawingRepository


@pytest.fixture(name="drawing_repository_empty")
def drawing_repository_empty_fixture(session_factory):
    repo = SQLAlchemyDrawingRepository(session=session_factory())
    return repo


@pytest.fixture(name="drawing_repository")
def drawing_repository_fixture(session_factory, drawings):
    repo = SQLAlchemyDrawingRepository(session=session_factory())
    drawings = drawings()
    for drawing in drawings:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(repo.add(drawing))
    return repo
