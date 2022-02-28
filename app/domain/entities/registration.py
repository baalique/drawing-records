from datetime import datetime

from app.domain.entities import AbstractEntity
from app.domain.entities.drawing import Drawing


class Registration(AbstractEntity):
    def __init__(self, id: int, drawing: Drawing):
        self.id = id
        self.drawing = drawing
        self.drawing_id = drawing.id
        self.created_at = datetime.now()
