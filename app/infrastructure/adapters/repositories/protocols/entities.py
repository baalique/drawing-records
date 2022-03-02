from app.domain.entities.drawing import Drawing
from app.infrastructure.adapters.repositories.protocols import (
    ReadOnlyRepository,
    WriteableRepository,
)
from app.service_layer.dtos.drawing import DrawingDtoCreate, DrawingDtoUpdate
from app.service_layer.dtos.registration import (
    RegistrationDtoCreate,
    RegistrationDtoOut,
)


class DrawingRepository(
    WriteableRepository[Drawing, DrawingDtoCreate, DrawingDtoUpdate]
):
    ...


class RegistrationRepository(
    ReadOnlyRepository[RegistrationDtoOut, RegistrationDtoCreate]
):
    ...
