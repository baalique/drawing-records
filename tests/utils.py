from typing import List, Any

from factory.base import FactoryMetaClass


def make_many(factory: FactoryMetaClass, amount) -> List[Any]:
    return [factory() for _ in range(amount)]
