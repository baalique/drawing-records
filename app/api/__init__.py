from fastapi import APIRouter

from app.api import health_check

router = APIRouter(prefix="/api/v1")

router.include_router(health_check.router)
