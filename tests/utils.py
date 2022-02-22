import asyncio
from contextlib import contextmanager
from typing import Any, List

from application import Application
from factory.base import FactoryMetaClass


def make_many(factory: FactoryMetaClass, amount) -> List[Any]:
    return [factory() for _ in range(amount)]


@contextmanager
def clear_database(app: Application):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(app.db.truncate_database())
    yield
    loop.run_until_complete(app.db.truncate_database())
