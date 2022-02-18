from adapters.repository.fake import FakeSession, FakeDatabase, FakeMetadata
from adapters.repository.fake.drawing import FakeDrawingRepository
from adapters.repository.fake.registration import FakeRegistrationRepository


def get_db():
    session = FakeSession()
    db = FakeDatabase(
        metadata=FakeMetadata(),
        repositories={
            "Drawing": FakeDrawingRepository(session),
            "Registration": FakeRegistrationRepository(session)
        }
    )
    return db


app_db = get_db()
