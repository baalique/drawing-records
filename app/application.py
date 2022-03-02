from dataclasses import dataclass

from fastapi import FastAPI

from app.config import Settings


@dataclass
class Application:
    app: FastAPI
    settings: Settings
