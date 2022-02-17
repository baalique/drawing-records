from fastapi import APIRouter

from api import drawing
from app.api import health_check
from config import get_current_app_settings

router = APIRouter(prefix=get_current_app_settings().API_PREFIX)

router.include_router(health_check.router)
router.include_router(drawing.router)
