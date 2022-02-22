from typing import Dict

from config import get_current_app_settings
from domain.entities.status import Status
from fastapi import APIRouter, status

router = APIRouter(prefix="/health-check", tags=["health-check"])


@router.get("/", status_code=status.HTTP_200_OK, response_model=Status)
def health_check() -> Dict[str, str]:
    settings = get_current_app_settings()
    return {
        "title": settings.PROJECT_TITLE,
        "description": settings.PROJECT_DESCRIPTION,
        "version": settings.PROJECT_VERSION,
    }
