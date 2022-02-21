import pytest
from fastapi import status
from fastapi.encoders import jsonable_encoder

from adapters.exceptions.exceptions import RelatedEntityNotExistsException


class TestRegistrationAPI:
    @pytest.mark.e2e
    def test_create_success(self, test_client, test_data, create_registration_dto):
        with test_client:
            drawing_id = test_data["Drawing"][0].id
            response = test_client.post(
                "registration/new",
                json=jsonable_encoder(create_registration_dto) | {"drawing_id": drawing_id}
            )
            data = response.json()

            assert response.status_code == status.HTTP_201_CREATED
            assert data["drawing"]["id"] == drawing_id

    @pytest.mark.e2e
    def test_create_fails_validation(self, test_client, test_data):
        with test_client:
            response = test_client.post(
                "registration/new",
                json={"wrong data": 0}
            )

            assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    @pytest.mark.e2e
    def test_create_fails_no_such_entity(self, test_client, test_data, create_registration_dto):
        with test_client:
            with pytest.raises(RelatedEntityNotExistsException):
                test_client.post(
                    "registration/new",
                    json=jsonable_encoder(create_registration_dto) | {"drawing_id": 1}
                )

    @pytest.mark.e2e
    def test_get_one_success(self, test_client, test_data):
        with test_client:
            registration_id = test_data["Registration"][0].id
            response = test_client.get(f"registration/{registration_id}")

            assert response.status_code == status.HTTP_200_OK

    @pytest.mark.e2e
    def test_get_one_fails_not_found(self, test_client):
        response = test_client.get(f"registration/{1}")

        assert response.status_code == status.HTTP_404_NOT_FOUND

    @pytest.mark.e2e
    def test_get_all_empty(self, test_client):
        with test_client:
            response = test_client.get("registration/all")
            data = response.json()

            assert response.status_code == status.HTTP_200_OK
            assert data == []

    @pytest.mark.e2e
    def test_get_all(self, test_client, test_data):
        with test_client:
            response = test_client.get("registration/all")
            data = response.json()

            assert response.status_code == status.HTTP_200_OK
            assert len(data) == len(test_data["Registration"])
