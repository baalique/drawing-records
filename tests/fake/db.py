from tests.fake.repositories import FakeDatabase, FakeSession
from tests.fake.repositories.drawing import FakeDrawingRepository
from tests.fake.repositories.registration import FakeRegistrationRepository


def get_db() -> FakeDatabase:
    session = FakeSession()
    db = FakeDatabase(
        repositories={
            "Drawing": FakeDrawingRepository(session),
            "Registration": FakeRegistrationRepository(session),
        },
    )
    return db


app_db = get_db()
