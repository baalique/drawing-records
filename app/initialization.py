from fastapi import FastAPI

from app import api
from app.application import Application
from app.config import Settings
from app.db import app_db
from app.infrastructure.adapters.repositories import AbstractDatabase


def init_database(settings: Settings) -> AbstractDatabase:
    return app_db


def init_app(settings: Settings) -> Application:
    fastapi_app = FastAPI(
        title=settings.PROJECT_TITLE,
        description=settings.PROJECT_DESCRIPTION,
        version=settings.PROJECT_VERSION,
        debug=settings.DEBUG,
    )

    fastapi_app.include_router(api.router)

    db = init_database(settings)

    return Application(app=fastapi_app, db=db, settings=settings)
