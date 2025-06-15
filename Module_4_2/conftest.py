import pytest
import requests
import json
from faker import Faker
from constant import BASE_URL
from constant import HEADERS
from constant import VALID_CREDENTIALS
from constant import INVALID_CREDENTIALS

fake = Faker()

@pytest.fixture(scope="session")
def auth_token():
    response = requests.post(f"{BASE_URL}/auth", json=VALID_CREDENTIALS)
    assert response.status_code == 200
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
