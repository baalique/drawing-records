from typing import Callable

import pytest

from adapters.repository import AbstractSession, AbstractRepository


@pytest.fixture(name="class_inherited_from_abstract_session")
def class_inherited_from_abstract_session_fixture() -> Callable[..., type]:
    return lambda **methods: type("TestSession", (AbstractSession,), methods)


@pytest.fixture(name="class_inherited_from_abstract_repository")
def class_inherited_from_abstract_repository_fixture() -> Callable[..., type]:
    return lambda **methods: type("TestRepository", (AbstractRepository,), methods)