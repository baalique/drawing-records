from typing import List

from fastapi import Depends
from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.entities.drawing import Drawing
from app.infrastructure.adapters.repositories.protocols.entities import (
    DrawingRepository,
)
from app.infrastructure.db.db import get_db
from app.service_layer.dtos.drawing import DrawingDtoUpdate


class SQLAlchemyDrawingRepository(DrawingRepository):
    def __init__(self, session: AsyncSession = Depends(get_db)):
        self.session = session

    async def add(self, drawing: Drawing) -> Drawing:
        async with self.session:
            self.session.add(drawing)
            await self.session.commit()
            return drawing

    async def get(self, id: int) -> Drawing:
        async with self.session:
            result = await self.session.execute(select(Drawing).where(Drawing.id == id))
            drawing = result.scalar()
            return drawing

    async def list(self) -> List[Drawing]:
        result = await self.session.execute(select(Drawing).order_by(Drawing.id))
        return result.scalars()

    async def update(self, drawing_update: DrawingDtoUpdate, id: int) -> Drawing:
        dict_to_update = {
            k: v for k, v in drawing_update.dict().items() if v is not None
        }

        _res = await self.session.execute(
            update(Drawing)
            .where(Drawing.id == id)
            .values(**dict_to_update)
            .returning(Drawing.id)
        )

        result_id = _res.scalar()
        await self.session.commit()

        result = await self.get(result_id)
        return result

    async def delete(self, id: int) -> bool:
        result = await self.session.execute(delete(Drawing).where(Drawing.id == id))
        await self.session.commit()
        return bool(result)
