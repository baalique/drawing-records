from fastapi import FastAPI

from app import api
from app.config import Settings, get_initial_app_settings
from app.infrastructure.adapters.orm import start_mappers
from app.infrastructure.db.db import get_session_factory
from app.infrastructure.protocols import UnitOfWork
from app.infrastructure.uow import SQLAlchemyUnitOfWork


def init_app(settings: Settings) -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_TITLE,
        description=settings.PROJECT_DESCRIPTION,
        version=settings.PROJECT_VERSION,
        debug=settings.DEBUG,
    )

    start_mappers()

    app.dependency_overrides[UnitOfWork] = SQLAlchemyUnitOfWork(
        get_session_factory(
            get_initial_app_settings().dsn, get_initial_app_settings().DB_ECHO
        )
    )

    app.include_router(api.get_router())

    return app
