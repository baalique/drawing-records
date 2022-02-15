from typing import Callable

from dotenv import load_dotenv
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    PROJECT_TITLE: str = Field(env="PROJECT_TITLE")
    PROJECT_DESCRIPTION: str = Field(env="PROJECT_DESCRIPTION")
    PROJECT_VERSION: str = Field(env="PROJECT_VERSION")

    DEBUG: bool = Field(env="DEBUG")
    LOG_LEVEL: str = Field(env="LOG_LEVEL")
    RELOAD: bool = Field(env="RELOAD")

    HOST_URL: str = Field(env="HOST_URL")
    HOST_PORT: int = Field(env="HOST_PORT")

    DB_URI: str = Field(env="DB_URI")
    DB_PORT: int = Field(env="DB_PORT")
    DB_USERNAME: str = Field(env="DB_USERNAME")
    DB_PASSWORD: str = Field(env="DB_PASSWORD")
    DB_NAME: str = Field(env="DB_NAME")

    @property
    def host(self) -> str:
        return f"http://{self.HOST_URL}:{self.HOST_PORT}"

    @property
    def dsn(self) -> str:
        return f"postgresql://{self.DB_USERNAME}:{self.DB_PASSWORD}@{self.DB_URI}:{self.DB_PORT}/{self.DB_NAME}"

    class Config:
        env_file = "../.env"
        env_file_encoding = "utf-8"


def _get_initial_app_settings() -> Callable[[], Settings]:
    load_dotenv()
    settings = Settings()

    return lambda: settings


get_initial_app_settings = _get_initial_app_settings()


def get_current_app_settings() -> Settings:
    return Settings()