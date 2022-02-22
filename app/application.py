from dataclasses import dataclass

from adapters.repository import AbstractDatabase
from config import Settings
from fastapi import FastAPI


@dataclass
class Application:
    app: FastAPI
    db: AbstractDatabase
    settings: Settings
