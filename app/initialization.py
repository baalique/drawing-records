from fastapi import FastAPI

import api
from config import Settings


def init_app(settings: Settings) -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_TITLE,
        description=settings.PROJECT_DESCRIPTION,
        version=settings.PROJECT_VERSION,
        debug=settings.DEBUG
    )
    app.include_router(api.router)
    return app
