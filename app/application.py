from dataclasses import dataclass

from fastapi import FastAPI

from app.adapters.repository import AbstractDatabase
from app.config import Settings


@dataclass
class Application:
    app: FastAPI
    db: AbstractDatabase
    settings: Settings
