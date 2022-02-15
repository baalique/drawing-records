import uvicorn
from fastapi import FastAPI

import api
from config import get_initial_app_settings

settings = get_initial_app_settings()

app = FastAPI(
    title=settings.PROJECT_TITLE,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION,
    debug=settings.DEBUG
)

app.include_router(api.router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST_URL,
        port=settings.HOST_PORT,
        reload=settings.RELOAD,
        log_level=settings.LOG_LEVEL
    )
