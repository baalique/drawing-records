from dataclasses import dataclass

from fastapi import FastAPI

from adapters.repository import AbstractDatabase
from config import Settings


@dataclass
class Application:
    app: FastAPI
    db: AbstractDatabase
    settings: Settings
