from fastapi import FastAPI

import api
from adapters.repository import AbstractDatabase, AbstractMetadata
from adapters.repository.fake import FakeDatabase, FakeMetadata
from api.drawing import drawing_repo
from application import Application
from config import Settings


def get_metadata(settings: Settings) -> AbstractMetadata:
    return FakeMetadata()


def init_database(settings: Settings) -> AbstractDatabase:
    metadata = get_metadata(settings)
    repositories = {
        "drawing": drawing_repo
    }
    return FakeDatabase(metadata, repositories)


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
