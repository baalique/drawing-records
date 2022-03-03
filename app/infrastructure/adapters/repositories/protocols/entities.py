from app.domain.entities.drawing import Drawing
from app.domain.entities.registration import Registration
from app.infrastructure.adapters.repositories.protocols import (
    ReadOnlyRepository,
    WriteableRepository,
)


class DrawingRepository(WriteableRepository[Drawing]):
    ...


class RegistrationRepository(ReadOnlyRepository[Registration]):
    ...
