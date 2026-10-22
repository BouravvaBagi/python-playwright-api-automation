
import os
import pytest
import requests

BASE_URL = "https://reqres.in/api"
API_KEY = os.getenv("REQRES_API_KEY")

pytestmark = pytest.mark.skipif(
    not API_KEY,
    reason="Set the REQRES_API_KEY environment variable"
)


@pytest.fixture
def headers():
    return {"x-api-key": API_KEY}


def test_list_users_success(headers):
    """Verify users list returns 200 and expected response fields."""
    response = requests.get(
        f"{BASE_URL}/users",
        params={"page": 2},
        headers=headers,
        timeout=10
    )

    assert response.status_code == 200
    body = response.json()
    assert "data" in body
    assert len(body["data"]) > 0
    assert body["page"] == 2
    assert "email" in body["data"][0]


def test_single_user_success(headers):
    """Verify user details and validate the response content."""
    response = requests.get(
        f"{BASE_URL}/users/2",
        headers=headers,
        timeout=10
    )

    assert response.status_code == 200
    body = response.json()
    assert "data" in body
    assert body["data"]["id"] == 2
    assert body["data"]["email"]


def test_nonexistent_user_returns_404(headers):
    """Verify error handling for an invalid user ID."""
    response = requests.get(
        f"{BASE_URL}/users/99999",
        headers=headers,
        timeout=10
    )

    assert response.status_code == 404
