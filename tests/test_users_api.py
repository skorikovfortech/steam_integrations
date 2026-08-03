from tests.fixture import create_user_data
from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_create_user(create_user_data):
    response = client.post(
        "/users/",
        json=create_user_data,
    )
    assert response.status_code == 200
