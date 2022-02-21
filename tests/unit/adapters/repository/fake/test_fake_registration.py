import pytest

from adapters.exceptions.exceptions import RelatedEntityNotExistsException


class TestFakeRegistrationRepository:
    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_initial_repository_empty(self, registration_repository_empty):
        result = await registration_repository_empty.list()
        assert result == []

    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_add_one_registration(self, registration_repository, create_registration_dto_from_repository):
        registration_repository = registration_repository(10)
        registrations = await registration_repository.list()
        start_len = len(registrations)

        await registration_repository.add(create_registration_dto_from_repository(registration_repository))
        new_registrations = await registration_repository.list()

        assert len(new_registrations) == start_len + 1

    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_add_one_registration_increases_pk(self, registration_repository,
                                                     create_registration_dto_from_repository):
        registration_repository = registration_repository(10)
        registrations = await registration_repository.list()

        start_max_id = max(d.id for d in registrations)

        new_registration = await registration_repository.add(
            create_registration_dto_from_repository(registration_repository))

        assert new_registration.id == start_max_id + 1

    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_add_one_registration_fails_no_such_drawing(self, registration_repository, create_registration_dto):
        registration_repository = registration_repository(10)
        drawings = await registration_repository.session._repositories["Drawing"].list()
        max_drawing_id = max(d.id for d in drawings)

        registration_create = create_registration_dto
        registration_create.drawing_id = max_drawing_id + 1

        with pytest.raises(RelatedEntityNotExistsException):
            await registration_repository.add(registration_create)

    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_get_one_registration(self, registration_repository, create_registration_dto_from_repository):
        registration_repository = registration_repository(10)
        registration = await registration_repository.add(
            create_registration_dto_from_repository(registration_repository))
        id_ = registration.id

        added_registration = await registration_repository.get(id_)

        assert registration == added_registration

    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_get_one_registration_fails(self, registration_repository):
        registration_repository = registration_repository(10)
        registrations = await registration_repository.list()
        max_id = max(d.id for d in registrations)

        result = await registration_repository.get(max_id + 1)

        assert result is None

    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_get_all_registrations(self, registration_repository):
        nb_of_registrations = 10

        registration_repository = registration_repository(nb_of_registrations)

        registrations = await registration_repository.list()

        assert len(registrations) == nb_of_registrations

    @pytest.mark.unit
    def test_call_registration_repository_returns_itself(self, registration_repository):
        registration_repository = registration_repository(10)
        assert registration_repository is registration_repository()

    @pytest.mark.unit
    @pytest.mark.asyncio
    async def test_truncate_database(self, registration_repository):
        registration_repository = registration_repository(10)
        await registration_repository.clear()
        registrations = await registration_repository.list()

        assert registrations == []
