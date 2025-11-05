import requests
from pydantic import BaseModel, field_validator
from typing import Optional
import random
from faker import Faker
import os
from dotenv import load_dotenv
from PythonProject2.venv.src.enums.const_url import ConstURL, AuthHeaders

load_dotenv()
fake = Faker('ru_RU')
BASE_URL = ConstURL.BASE_URL.value
LOGIN_URL =  ConstURL.LOGIN_URL.value

class RequestItem (BaseModel):
    title: str
    description: Optional[str] = None

    """ Функции для генерации тестовых данных"""
    @classmethod
    def item_data(cls) -> "RequestItem":
        object_item = cls(
            title=fake.text(max_nb_chars=10),
            description=fake.text(max_nb_chars=random.randint
            (5, 10))
            if random.choice([True, False])
            else None
        )
        return object_item.model_dump()

    @classmethod
    def update_item_data(cls) -> "RequestItem":
        object_item = cls(
            title=fake.text(max_nb_chars=20),
            description=fake.text(max_nb_chars=random.randint
            (15, 20))
            if random.choice([True, False])
            else None
        )
        return object_item.model_dump()

"""Класс генерации невалидиных данных"""
class WrongItems(BaseModel):
    title: str
    description: Optional[str] = None

    @classmethod
    def wrong_item_data(cls):
        length_text = random.randint(256, 299)
        wrong_text = fake.text(max_nb_chars=length_text)
        object_data = cls(
            title=wrong_text,
            description=fake.text(max_nb_chars=15)
        )
        return object_data

class NoneItems(BaseModel):
    title: None
    description: Optional[str] = None

    @classmethod
    def none_item_data(cls) -> "NoneItems":
        object_item = cls(
            title=None,
            description=fake.text(max_nb_chars=random.randint
            (1, 25))
            if random.choice([True, False])
            else None
        )
        return object_item.model_dump()

"""Класс получаемых данных"""
class ResponseItem (BaseModel):
    title: str
    description: Optional[str] = None
    id: str
    owner_id: str

class ResponseUserItems(BaseModel):
    data: list[ResponseItem]
    count: int

    @field_validator('count')
    def count_must_match_data_length(cls, v, values):
        data = values.get('data')
        if data is None:
            raise ValueError('Поле data должно содержать данные для сверки')
        if v != len(data):
            raise ValueError(f'Количество элементов ({v}) не соответствует количеству элементов данных ({len(data)})')
        return v

# Внимание дублирование кода всего класса
"""Класс генерации авторизации"""
class AuthData:
    def auth_item_data(self):
        """Создаем валидные данные для авторизации"""
        return  {"username": os.getenv("VALID_USERNAME"), "password": os.getenv("VALID_PASSWORD")}
        # return AuthHeaders.AUTH_DATA.value

# auth = AuthData()
# auth_data = auth.auth_item_data()
# print(auth_data)

    def auth_wrong_data(self):
        """Невалидные данные для авторизации"""
        return  {"username": os.getenv("INVALID_USERNAME"), "password": os.getenv("INVALID_PASSWORD")}

# auth = AuthData()
# auth_data = auth.auth_wrong_data()
# print(auth_data)

    def auth_header_data(self):
        """Создаем валидные данные для авторизации"""
        return AuthHeaders.AUTH_HEADERS.value

# auth = AuthData()
# auth_data = auth.auth_header_data()
# print(auth_data)

    def auth_token(self):
        """Создание сессию с авторизацией"""
        token_session = requests.Session()
        auth_data = AuthHeaders.AUTH_DATA.value
        auth_headers = AuthHeaders.AUTH_HEADERS.value
        response = token_session.post(LOGIN_URL, headers=auth_headers, data=auth_data)
        response.raise_for_status()
        items_token = response.json()["access_token"]
        token_session.headers.update({"Authorization": f"Bearer {items_token}"})
        return token_session

# auth= AuthData()
# session = auth.auth_token()
#
# print(f'объект= {session}')  # выведет информацию об объекте Session
# print(f'хеддеры = {session.headers}')  # выведет заголовки, включая токен авторизации

