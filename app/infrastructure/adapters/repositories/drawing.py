from typing import Any, Dict, List, Optional

from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.entities.drawing import Drawing
from app.infrastructure.adapters.repositories.protocols.entities import (
    DrawingRepository,
)


class SQLAlchemyDrawingRepository(DrawingRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, drawing: Drawing) -> Drawing:
        self.session.add(drawing)
        return drawing

    async def get(self, id: int) -> Optional[Drawing]:
        result = await self.session.execute(select(Drawing).where(Drawing.id == id))
        drawing = result.scalar()
        return drawing

    async def list(self) -> List[Drawing]:
        result = await self.session.execute(select(Drawing).order_by(Drawing.id))
        return result.scalars().all()

    async def update(self, id: int, update_dict: Dict[str, Any]) -> Optional[Drawing]:
        _res = await self.session.execute(
            update(Drawing)
            .where(Drawing.id == id)
            .values(**update_dict)
            .returning(Drawing.id)
        )

        result_id = _res.scalar()

        if result_id:
            result = await self.get(result_id)
            return result
        else:
            return None

    async def delete(self, id: int) -> bool:
        _res = await self.session.execute(
            delete(Drawing).where(Drawing.id == id).returning(Drawing.id)
        )
        result = _res.scalar()
        return bool(result)
