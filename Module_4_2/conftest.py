import pytest
import requests
import json
from faker import Faker

from PythonProject.constant import HEADERS, BASE_URL

# from constant import BASE_URL
# from constant import HEADERS
# from constant import VALID_CREDENTIALS
# from constant import INVALID_CREDENTIALS

fake = Faker()

@pytest.fixture(scope="session")
def auth_token():
    response = requests.post(f"{BASE_URL}/auth", json=VALID_CREDENTIALS)
    assert response.status_code == 200, "Ошибочный статус-код"
    return response.json()["token"]

@pytest.fixture(scope="session")
def booking_data():
    return {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "totalprice": fake.random_int(min=100, max=10000),
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-04-05",
            "checkout": "2024-04-08"
        },
        "additionalneeds": "Breakfast"
    }

# Фикстура для создания бронирования и возврата bookingid
@pytest.fixture(scope="session")
def booking_id(booking_data):
    response = requests.post(f"{BASE_URL}/booking", json=booking_data)
    assert response.status_code == 200
    return response.json()["bookingid"]

@pytest.fixture(scope="session")
def auth_session():
    """Create session with authorization and return session`s object """
    session = requests.Session()
    session.headers.update(HEADERS)

    auth_response = session.post(f'{BASE_URL}/auth', json={"username": "admin", "password": "password123"})
    token = auth_response.json().get("token")
    assert token is not None, "Токен в ответе отсутствует"

    session.headers.update({"Cookie": f"token={token}"})
    return session