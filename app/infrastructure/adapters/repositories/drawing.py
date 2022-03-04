from typing import Any, Dict, List, Optional

from fastapi import Depends
from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.entities.drawing import Drawing
from app.infrastructure.adapters.repositories.protocols.entities import (
    DrawingRepository,
)
from app.infrastructure.db.db import get_db


class SQLAlchemyDrawingRepository(DrawingRepository):
    def __init__(self, session: AsyncSession = Depends(get_db)):
        self.session = session

    async def add(self, drawing: Drawing) -> Drawing:
        async with self.session:
            self.session.add(drawing)
            await self.session.commit()
            return drawing

    async def get(self, id: int) -> Optional[Drawing]:
        async with self.session:
            result = await self.session.execute(select(Drawing).where(Drawing.id == id))
            drawing = result.scalar()
            return drawing

    async def list(self) -> List[Drawing]:
        async with self.session:
            result = await self.session.execute(select(Drawing).order_by(Drawing.id))
            return result.scalars().all()

    async def update(self, id: int, update_dict: Dict[str, Any]) -> Optional[Drawing]:
        async with self.session:
            _res = await self.session.execute(
                update(Drawing)
                .where(Drawing.id == id)
                .values(**update_dict)
                .returning(Drawing.id)
            )

            result_id = _res.scalar()
            await self.session.commit()

            if result_id:
                result = await self.get(result_id)
                return result
            else:
                return None

    async def delete(self, id: int) -> bool:
        async with self.session:
            _res = await self.session.execute(
                delete(Drawing).where(Drawing.id == id).returning(Drawing.id)
            )
            result = _res.scalar()
            await self.session.commit()
            return bool(result)
