from factory import Factory, Faker, SubFactory

from app.service_layer.dtos.registration import (
    RegistrationDtoCreate,
    RegistrationDtoOut,
)
from tests.factories.entities.drawing import FactoryDrawing


class FactoryRegistration(Factory):
    id = Faker("pyint", min_value=1)
    drawing = SubFactory(FactoryDrawing)
    created_at = Faker("date_time_this_decade")

    class Meta:
        model = RegistrationDtoOut


class FactoryRegistrationCreate(Factory):
    drawing_id = Faker("pyint", min_value=1)
    created_at = Faker("date_time_this_decade")

    class Meta:
        model = RegistrationDtoCreate
