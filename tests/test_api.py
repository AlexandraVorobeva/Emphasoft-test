from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_authentication_of_user():
    response = client.post(
        "/auth/sign-up/",
        json={
            "email": "alexandra@gmail.com",
            "username": "alexandra",
            "first_name": "alexandra",
            "last_name": "vorobeva",
            "password": "12345"
        },
    )
    assert response.status_code == 200, response.text


def test_authentication_of_user_negative():
    response = client.post(
        "/auth/sign-up/"
    )
    assert response.status_code == 422, response.text


def test_get_all_users_negative():
    response = client.get("/users/")
    assert response.status_code == 401, response.text


def test_create_user_negative():
    response = client.post("/")
    assert response.status_code == 404, response.text

