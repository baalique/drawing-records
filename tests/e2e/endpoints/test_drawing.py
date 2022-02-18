import pytest
from fastapi import status
from fastapi.encoders import jsonable_encoder


class TestDrawingAPI:
    @pytest.mark.e2e
    def test_create_success(self, test_client, create_drawing_dto):
        with test_client:
            response = test_client.post(
                "drawing/new",
                json=jsonable_encoder(create_drawing_dto)
            )
            data = response.json()

            assert response.status_code == status.HTTP_201_CREATED
            assert data["id"] == 1

    @pytest.mark.e2e
    def test_create_fails_validation(self, test_client):
        with test_client:
            response = test_client.post(
                "drawing/new",
                json={"wrong data": 0}
            )

            assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    @pytest.mark.e2e
    def test_get_one_success(self, test_client, create_drawing_dto):
        with test_client:
            create_response = test_client.post(
                "drawing/new",
                json=jsonable_encoder(create_drawing_dto)
            )
            id_ = create_response.json()["id"]
            response = test_client.get(f"drawing/{id_}")

            assert response.status_code == status.HTTP_200_OK

    @pytest.mark.e2e
    def test_get_one_fails_not_found(self, test_client):
        response = test_client.get(f"drawing/{1}")

        assert response.status_code == status.HTTP_404_NOT_FOUND

    @pytest.mark.e2e
    def test_get_all_empty(self, test_client):
        with test_client:
            response = test_client.get("drawing/all")
            data = response.json()

            assert response.status_code == status.HTTP_200_OK
            assert data == []

    @pytest.mark.e2e
    def test_get_all(self, test_client, create_many_drawing_dto):
        drawings = create_many_drawing_dto()
        with test_client:
            for dto in drawings:
                test_client.post(
                    "drawing/new",
                    json=jsonable_encoder(dto)
                )
            response = test_client.get("drawing/all")
            data = response.json()

            assert response.status_code == status.HTTP_200_OK
            assert len(data) == len(drawings)

    @pytest.mark.e2e
    def test_update_success(self, test_client, create_drawing_dto, update_drawing_dto):
        with test_client:
            create_response = test_client.post(
                "drawing/new",
                json=jsonable_encoder(create_drawing_dto)
            )
            id_ = create_response.json()["id"]

            response = test_client.patch(
                f"drawing/{id_}",
                json=jsonable_encoder(update_drawing_dto)
            )

            assert response.status_code == status.HTTP_200_OK
            assert all(response.json()[key] == update_drawing_dto.dict()[key] for key in
                       ("name", "category", "project"))

    @pytest.mark.e2e
    def test_update_fails_not_found(self, test_client, update_drawing_dto):
        with test_client:
            response = test_client.patch(
                "drawing/1",
                json=jsonable_encoder(update_drawing_dto)
            )

            assert response.status_code == status.HTTP_404_NOT_FOUND

    @pytest.mark.e2e
    def test_update_wrong_data_not_affect(self, test_client, create_drawing_dto, update_drawing_dto):
        with test_client:
            create_response = test_client.post(
                "drawing/new",
                json=jsonable_encoder(create_drawing_dto)
            )
            id_ = create_response.json()["id"]

            drawing_1_response = test_client.get(f"drawing/{id_}")
            update_response = test_client.patch(
                f"drawing/{id_}",
                json={"wrong data": 0}
            )
            drawing_2_response = test_client.get(f"drawing/{id_}")

            assert update_response.status_code == status.HTTP_200_OK
            assert drawing_1_response.json() == drawing_2_response.json()

    @pytest.mark.e2e
    def test_delete_success(self, test_client, create_drawing_dto):
        with test_client:
            create_response = test_client.post(
                "drawing/new",
                json=jsonable_encoder(create_drawing_dto)
            )
            id_ = create_response.json()["id"]

            delete_response = test_client.delete(f"drawing/{id_}")

            get_response = test_client.get(f"drawing/{id_}")

            assert delete_response.status_code == status.HTTP_204_NO_CONTENT
            assert get_response.status_code == status.HTTP_404_NOT_FOUND

    @pytest.mark.e2e
    def test_delete_fails_not_found(self, test_client):
        with test_client:
            response = test_client.delete("drawing/1")

            assert response.status_code == status.HTTP_404_NOT_FOUND
