from dataclasses import dataclass

from fastapi import FastAPI

from app.config import Settings
from app.infrastructure.adapters.repositories import AbstractDatabase


@dataclass
class Application:
    app: FastAPI
    db: AbstractDatabase
    settings: Settings
