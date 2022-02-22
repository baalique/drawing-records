from app.adapters.repository.fake import FakeDatabase, FakeMetadata, FakeSession
from app.adapters.repository.fake.drawing import FakeDrawingRepository
from app.adapters.repository.fake.registration import FakeRegistrationRepository


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
