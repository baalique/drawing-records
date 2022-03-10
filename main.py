import uvicorn

from app.config import get_initial_app_settings
from app.initialization import init_app

app_settings = get_initial_app_settings()
app = init_app(app_settings)


def start_app() -> None:
    settings = app_settings
    uvicorn.run(
        "main:app",
        host=settings.HOST_URL,
        port=settings.HOST_PORT,
        reload=settings.RELOAD,
        log_level=settings.LOG_LEVEL,
    )


if __name__ == "__main__":
    start_app()
