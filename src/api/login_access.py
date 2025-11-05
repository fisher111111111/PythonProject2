import requests
from dotenv import load_dotenv
from PythonProject2.src.enums.const_url import ConstURL, AuthHeaders

load_dotenv()

class AuthLogin:
    def  __init__(self, auth_session):
        self.headers = AuthHeaders.AUTH_HEADERS.value
        self.login = ConstURL.LOGIN_URL.value
        self.auth_session = auth_session

    def create_token(self):
        """Создаем валидные данные для авторизации"""
        auth_data = AuthHeaders.AUTH_DATA.value
        response_token = self.auth_session.post(self.login, headers=self.headers, data=auth_data)
        return response_token

# session = requests.Session()
# auth = AuthLogin(session)
# response = auth.create_token()
# print(response.text)

"""Закомментированные негативные кейсы получения токена выносим в сценарии и покрываем сценарии тестами"""
#     def wrong_create_token(self):
#         """Создаем валидные данные для авторизации"""
#         auth_data = {
#             "username": os.getenv("VALID_USERNAME"),
#             "password": os.getenv("VALID_PASSWORD"),
#             "grant_type": ""
#         }
#         response = self.auth_session.post(f'{self.base_url}{self.login}', data=auth_data)
#         return response
#
# session = requests.Session()
# auth = AuthLogin(session)
# response = auth.wrong_create_token()
# print(response.status_code, response.text)

#     def auth_wrong_data(self):
#         """Невалидные данные для авторизации"""
#         auth_wrong = {
#             "username": os.getenv("INVALID_USERNAME"),
#             "password": os.getenv("INVALID_PASSWORD")
#         }
#         response = self.auth_session.post(f'{self.base_url}{self.login}', data=auth_wrong)
#         return response
#
# # session = requests.Session()
# # auth = AuthLogin(session)
# # response = auth.auth_wrong_data()
# # print(response.status_code, response.text)
#
#     def non_auth_data(self):
#         """Отправляет запрос на создание токена аутентификации."""
#         none_auth = {
#             "username": os.getenv("None"),
#             "password": os.getenv("None")
#         }
#         response = self.auth_session.post(f'{self.base_url}{self.login}', data=none_auth)
#         return response

# session = requests.Session()
# auth = AuthLogin(session)
# response = auth.auth_wrong_data()
# print(response.status_code, response.text)