import pytest
from fastapi import status
from fastapi.encoders import jsonable_encoder


@pytest.mark.e2e
def test_create_success(test_client, drawing_dto_create):
    with test_client:
        response = test_client.post(
            "drawing/new", json=jsonable_encoder(drawing_dto_create)
        )
        data = response.json()

        assert response.status_code == status.HTTP_201_CREATED
        assert data["id"] == drawing_dto_create.id


@pytest.mark.e2e
def test_create_fails_parent_not_found(test_client, drawing_dto_create):
    with test_client:
        drawing_dto_create.parent_id = drawing_dto_create.id + 1

        response = test_client.post(
            "drawing/new", json=jsonable_encoder(drawing_dto_create)
        )

        assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.e2e
def test_create_fails_already_exists(test_client, drawings_dto_create):
    with test_client:
        drawing_create_1, drawing_create_2 = drawings_dto_create(2)
        test_client.post("drawing/new", json=jsonable_encoder(drawing_create_1))
        drawing_create_2.id = drawing_create_1.id

        response = test_client.post(
            "drawing/new", json=jsonable_encoder(drawing_create_2)
        )

        assert response.status_code == status.HTTP_409_CONFLICT


@pytest.mark.e2e
def test_create_fails_validation(test_client):
    with test_client:
        response = test_client.post("drawing/new", json={"wrong data": 0})

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


@pytest.mark.e2e
def test_get_one_success(test_client, drawing_dto_create):
    with test_client:
        create_response = test_client.post(
            "drawing/new", json=jsonable_encoder(drawing_dto_create)
        )
        id_ = create_response.json()["id"]

        response = test_client.get(f"drawing/{id_}")

        assert response.status_code == status.HTTP_200_OK


@pytest.mark.e2e
def test_get_one_fails_not_found(test_client):
    response = test_client.get(f"drawing/{1}")

    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.e2e
def test_get_all_empty(test_client):
    with test_client:
        response = test_client.get("drawing/all")
        data = response.json()

        assert response.status_code == status.HTTP_200_OK
        assert data == []


@pytest.mark.e2e
def test_get_all(test_client, drawings_dto_create):
    drawings = drawings_dto_create()
    with test_client:
        for dto in drawings:
            test_client.post("drawing/new", json=jsonable_encoder(dto))

        response = test_client.get("drawing/all")
        data = response.json()

        assert response.status_code == status.HTTP_200_OK
        assert len(data) == len(drawings)


@pytest.mark.e2e
def test_update_success(test_client, drawing_dto_create, drawing_dto_update):
    with test_client:
        create_response = test_client.post(
            "drawing/new", json=jsonable_encoder(drawing_dto_create)
        )
        id_ = create_response.json()["id"]

        response = test_client.patch(
            f"drawing/{id_}", json=jsonable_encoder(drawing_dto_update)
        )

        assert response.status_code == status.HTTP_200_OK
        assert all(
            response.json()[key] == drawing_dto_update.dict()[key]
            for key in ("name", "category", "project")
        )


@pytest.mark.e2e
def test_update_fails_not_found(test_client, drawing_dto_update):
    with test_client:
        response = test_client.patch(
            "drawing/1", json=jsonable_encoder(drawing_dto_update)
        )

        assert response.status_code == status.HTTP_404_NOT_FOUND


def test_update_fails_parent_not_found(
    test_client, drawing_dto_create, drawing_dto_update
):
    with test_client:
        create_response = test_client.post(
            "drawing/new", json=jsonable_encoder(drawing_dto_create)
        )
        id_ = create_response.json()["id"]
        drawing_dto_update.parent_id = id_ + 1

        response = test_client.patch(
            f"drawing/{id_}", json=jsonable_encoder(drawing_dto_update)
        )

        assert response.status_code == status.HTTP_404_NOT_FOUND


def test_update_fails_already_exists(
    test_client, drawings_dto_create, drawing_dto_update
):
    with test_client:
        drawing_create_1, drawing_create_2 = drawings_dto_create(2)
        test_client.post("drawing/new", json=jsonable_encoder(drawing_create_1))
        test_client.post("drawing/new", json=jsonable_encoder(drawing_create_2))
        drawing_dto_update.id = drawing_create_2.id

        response = test_client.patch(
            f"drawing/{drawing_create_1.id}", json=jsonable_encoder(drawing_dto_update)
        )

        assert response.status_code == status.HTTP_409_CONFLICT


@pytest.mark.e2e
def test_update_wrong_data_not_affect(
    test_client, drawing_dto_create, drawing_dto_update
):
    with test_client:
        create_response = test_client.post(
            "drawing/new", json=jsonable_encoder(drawing_dto_create)
        )
        id_ = create_response.json()["id"]

        drawing_1_response = test_client.get(f"drawing/{id_}")
        test_client.patch(f"drawing/{id_}", json={"wrong data": 0})
        drawing_2_response = test_client.get(f"drawing/{id_}")

        assert drawing_1_response.json() == drawing_2_response.json()


@pytest.mark.e2e
def test_update_fails_validation(test_client, drawing_dto_create):
    with test_client:
        create_response = test_client.post(
            "drawing/new", json=jsonable_encoder(drawing_dto_create)
        )
        id_ = create_response.json()["id"]

        response = test_client.patch(f"drawing/{id_}", json={"wrong data": 0})

        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


@pytest.mark.e2e
def test_delete_success(test_client, drawing_dto_create):
    with test_client:
        create_response = test_client.post(
            "drawing/new", json=jsonable_encoder(drawing_dto_create)
        )
        id_ = create_response.json()["id"]

        delete_response = test_client.delete(f"drawing/{id_}")
        get_response = test_client.get(f"drawing/{id_}")

        assert delete_response.status_code == status.HTTP_204_NO_CONTENT
        assert get_response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.e2e
def test_delete_fails_not_found(test_client):
    with test_client:
        response = test_client.delete("drawing/1")

        assert response.status_code == status.HTTP_404_NOT_FOUND
