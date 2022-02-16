from fastapi import APIRouter

from api import drawing
from app.api import health_check

router = APIRouter(prefix="/api/v1")

router.include_router(health_check.router)
router.include_router(drawing.router)
