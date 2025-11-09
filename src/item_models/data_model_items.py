import requests
from pydantic import BaseModel, field_validator
from typing import Optional
import random
import string
from faker import Faker
import os
from dotenv import load_dotenv
from PythonProject2.src.enums_item.const_url import ConstURL, AuthHeaders

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
        '''Генерация данный для создания итем'''
        object_item = cls(
            title=fake.text(max_nb_chars=10),
            description=fake.text(max_nb_chars=random.randint
            (5, 10))
            if random.choice([True, False])
            else None
        )
        return object_item.model_dump()

# object_data = RequestItem.item_data()
# print(f'item_data = {object_data}')


    @classmethod
    def update_item_data(cls) -> "RequestItem":
        '''Генерация данных для обновления итем'''
        object_item = cls(
            title=fake.text(max_nb_chars=20),
            description=fake.text(max_nb_chars=random.randint
            (15, 20))
            if random.choice([True, False])
            else None
        )
        return object_item.model_dump()

    @classmethod
    def params_valid(cls):  # далее не стал делать невалидные данные для params, т.к. параметры работают некорректно!!!
        '''Генерация не дефолтных параметров для проверки работоспособности выборки сервера'''
        skip = random.randint(0, 10)
        limit = random.randint(11, 19)
        return {"skip": skip, "limit": limit}

"""Класс генерации невалидиных данных"""
class WrongItems(BaseModel):
    '''
    генерация данных где  более 255 символов для значения "title"
    '''
    title: str
    description: Optional[str] = None

    @classmethod
    def too_long_data(cls) -> "WrongItems":
        length = random.randint(256, 299)
        letters = string.ascii_letters + string.digits + string.punctuation + ' '
        result = ''.join(random.choices(letters, k=length))
        object_data = cls(
                    title=result,
                    description=fake.text(max_nb_chars=15)
                )
        return object_data.model_dump()

# object_data = WrongItems.too_long_data()
# print(f'too_long_data = {object_data}')
# print(f"too_long_data len = {len(object_data['title'])}")


class NoneItems(BaseModel):
    ''' генерация данных, где "title" равно None '''
    title: None
    description: Optional[str] = None

    @classmethod
    def none_item_data(cls) -> "NoneItems":
        object_item = cls(
            title=None,
            description=fake.text(max_nb_chars=15)
        )
        return object_item.model_dump()

# object_data = NoneItems.none_item_data()
# print(f'non_item_data = {object_data}')

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
        response = token_session.post(LOGIN_URL,
                                      headers=auth_headers,
                                      data=auth_data)
        response.raise_for_status()
        items_token = response.json()["access_token"]
        token_session.headers.update({"Authorization": f"Bearer {items_token}"})
        return token_session

# auth= AuthData()
# session = auth.auth_token()
# print(f'объект= {session}')  # выведет информацию об объекте Session
# print(f'хеддеры = {session.headers}')  # выведет заголовки, включая токен авторизации

    def auth_empty_token(self):
        """Создание сессию с авторизацией"""
        token_session = requests.Session()
        auth_data = AuthHeaders.AUTH_DATA.value
        auth_headers = AuthHeaders.AUTH_HEADERS.value
        response = token_session.post(LOGIN_URL,
                                      headers=auth_headers,
                                      data=auth_data)
        response.raise_for_status()
        token_session.headers.update({"Authorization": f""})
        print( token_session.headers)
        return token_session

# auth= AuthData()
# session = auth.auth_empty_token()
# print(f'объект= {session}')