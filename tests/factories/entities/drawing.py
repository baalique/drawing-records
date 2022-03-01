from factory import Factory, Faker

from app.service_layer.dtos.drawing import (
    DrawingDtoCreate,
    DrawingDtoOut,
    DrawingDtoUpdate,
)


class FactoryDrawing(Factory):
    id = Faker("pyint", min_value=1)
    name = Faker("pystr", min_chars=1, max_chars=255)
    parent = None
    category = Faker("pystr", min_chars=1, max_chars=255)
    project = Faker("pystr", min_chars=1, max_chars=255)
    drawing_data = Faker("pydict")
    path_to_file = Faker("file_path")

    class Meta:
        model = DrawingDtoOut


class FactoryDrawingCreate(Factory):
    name = Faker("pystr", min_chars=1, max_chars=255)
    parent = Faker("pyint", min_value=0)
    category = Faker("pystr", min_chars=1, max_chars=255)
    project = Faker("pystr", min_chars=1, max_chars=255)
    drawing_data = Faker("pydict")
    path_to_file = Faker("file_path")

    class Meta:
        model = DrawingDtoCreate


class FactoryDrawingUpdate(Factory):
    name = Faker("pystr", min_chars=1, max_chars=255)
    parent = Faker("pyint", min_value=0)
    category = Faker("pystr", min_chars=1, max_chars=255)
    project = Faker("pystr", min_chars=1, max_chars=255)
    drawing_data = Faker("pydict")
    path_to_file = Faker("file_path")

    class Meta:
        model = DrawingDtoUpdate
