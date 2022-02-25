from app.infrastructure.adapters.repositories.fake import (
    FakeDatabase,
    FakeMetadata,
    FakeSession,
)
from app.infrastructure.adapters.repositories.fake.drawing import FakeDrawingRepository
from app.infrastructure.adapters.repositories.fake.registration import (
    FakeRegistrationRepository,
)


def get_db() -> FakeDatabase:
    session = FakeSession()
    db = FakeDatabase(
        metadata=FakeMetadata(),
        repositories={
            "Drawing": FakeDrawingRepository(session),
            "Registration": FakeRegistrationRepository(session),
        },
    )
    return db


app_db = get_db()
