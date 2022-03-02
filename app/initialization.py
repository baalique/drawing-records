from fastapi import FastAPI

from app import api
from app.application import Application
from app.config import Settings


def init_app(settings: Settings) -> Application:
    fastapi_app = FastAPI(
        title=settings.PROJECT_TITLE,
        description=settings.PROJECT_DESCRIPTION,
        version=settings.PROJECT_VERSION,
        debug=settings.DEBUG,
    )

    fastapi_app.include_router(api.router)

    return Application(app=fastapi_app, settings=settings)
