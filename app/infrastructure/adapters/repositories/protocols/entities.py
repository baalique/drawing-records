from app.infrastructure.adapters.repositories.protocols import (
    ReadOnlyRepository,
    WriteableRepository,
)
from app.service_layer.dtos.drawing import (
    DrawingDtoCreate,
    DrawingDtoOut,
    DrawingDtoUpdate,
)
from app.service_layer.dtos.registration import RegistrationCreate, RegistrationDtoOut


class DrawingRepository(
    WriteableRepository[DrawingDtoOut, DrawingDtoCreate, DrawingDtoUpdate]
):
    ...


class RegistrationRepository(
    ReadOnlyRepository[RegistrationDtoOut, RegistrationCreate]
):
    ...
