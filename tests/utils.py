from contextlib import asynccontextmanager
from typing import List, Any

from factory.base import FactoryMetaClass

from application import Application


def make_many(factory: FactoryMetaClass, amount) -> List[Any]:
    return [factory() for _ in range(amount)]


@asynccontextmanager
async def clear_database(app: Application):
    await app.db.truncate_database()
    yield
    await app.db.truncate_database()
