from factory import Factory, Faker

from app.domain.entities.drawing import Drawing


class FactoryDrawing(Factory):
    id = Faker("pyint", min_value=1)
    name = Faker("pystr", min_chars=1, max_chars=255)
    parent = None
    category = Faker("pystr", min_chars=1, max_chars=255)
    project = Faker("pystr", min_chars=1, max_chars=255)
    drawing_data = Faker("pydict")
    path_to_file = Faker("file_path")

    class Meta:
        model = Drawing
