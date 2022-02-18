import pytest
from fastapi import status


@pytest.mark.e2e
def test_healthcheck(test_client):
    with test_client:
        response = test_client.get("health-check")
        assert response.status_code == status.HTTP_200_OK
