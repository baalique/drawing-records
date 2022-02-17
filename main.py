import uvicorn

from config import get_initial_app_settings, get_current_app_settings
from initialization import init_app

app_settings = get_initial_app_settings()
app = init_app(app_settings)

fastapi_app = app.app


def start_app() -> None:
    settings = get_current_app_settings()
    uvicorn.run(
        "main:fastapi_app",
        host=settings.HOST_URL,
        port=settings.HOST_PORT,
        reload=settings.RELOAD,
        log_level=settings.LOG_LEVEL
    )


if __name__ == "__main__":
    start_app()
