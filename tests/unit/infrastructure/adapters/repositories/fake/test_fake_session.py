import pytest

from tests.fake.exceptions import FakeInvalidEntityError


class TestFakeSession:
    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_add_session_fails_wrong_type(self, fake_session):
        with pytest.raises(FakeInvalidEntityError):
            await fake_session.add("test data")

    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_get_session_fails_wrong_type(self, fake_session):
        with pytest.raises(FakeInvalidEntityError):
            await fake_session.get("test data", None)

    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_get_all_session_fails_wrong_type(self, fake_session):
        with pytest.raises(FakeInvalidEntityError):
            await fake_session.list("test data")

    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_update_session_fails_wrong_type(self, fake_session):
        with pytest.raises(FakeInvalidEntityError):
            await fake_session.update("test data", None)

    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_delete_session_fails_wrong_type(self, fake_session):
        with pytest.raises(FakeInvalidEntityError):
            await fake_session.delete("test data", None)
