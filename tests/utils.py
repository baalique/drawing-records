import asyncio
from contextlib import contextmanager
from typing import Any, Callable, List, Optional

from factory.base import FactoryMetaClass

from app.application import Application


def make_many(
    factory: FactoryMetaClass,
    amount: int,
    primary_key_expression: Optional[Callable[[FactoryMetaClass], Any]] = None,
) -> List[Any]:
    if not primary_key_expression:
        return [factory() for _ in range(amount)]

    objs = []
    _pks = {}
    c = 0
    while True:
        if c >= amount:
            return objs
        obj = factory()
        if primary_key_expression(obj) not in _pks:
            objs.append(obj)
            c += 1


@contextmanager
def clear_database(app: Application):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(app.db.truncate_database())
    yield
    loop.run_until_complete(app.db.truncate_database())
