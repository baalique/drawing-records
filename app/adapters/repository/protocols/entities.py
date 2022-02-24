from app.adapters.repository.protocols import ReadOnlyRepository, WriteableRepository
from app.domain.entities.drawing import Drawing, DrawingCreate, DrawingUpdate
from app.domain.entities.registration import Registration, RegistrationCreate


class DrawingRepository(WriteableRepository[Drawing, DrawingCreate, DrawingUpdate]):
    ...


class RegistrationRepository(ReadOnlyRepository[Registration, RegistrationCreate]):
    ...
