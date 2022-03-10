from fastapi import APIRouter

from app.api import drawing, health_check, registration
from app.config import get_initial_app_settings


def get_router() -> APIRouter:
    router = APIRouter(prefix=get_initial_app_settings().API_PREFIX)

    router.include_router(health_check.router)
    router.include_router(drawing.router)
    router.include_router(registration.router)
    return router
