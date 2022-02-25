from app.domain.entities.drawing import Drawing, DrawingCreate, DrawingUpdate
from app.domain.entities.registration import Registration, RegistrationCreate
from app.infrastructure.adapters.repositories.protocols import (
    ReadOnlyRepository,
    WriteableRepository,
)


class DrawingRepository(WriteableRepository[Drawing, DrawingCreate, DrawingUpdate]):
    ...


class RegistrationRepository(ReadOnlyRepository[Registration, RegistrationCreate]):
    ...
