from fastapi import FastAPI

import api
from adapters.repository import AbstractDatabase
from application import Application
from config import Settings
from db import app_db


def init_database(settings: Settings) -> AbstractDatabase:
    return app_db


def init_app(settings: Settings) -> Application:
    fastapi_app = FastAPI(
        title=settings.PROJECT_TITLE,
        description=settings.PROJECT_DESCRIPTION,
        version=settings.PROJECT_VERSION,
        debug=settings.DEBUG
    )

    fastapi_app.include_router(api.router)

    db = init_database(settings)

    return Application(
        app=fastapi_app,
        db=db,
        settings=settings
    )
