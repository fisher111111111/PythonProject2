# модуль для проверки различных вариантов кода
from PythonProject2.src.enums_item.const_url import ConstURL, ApiHeaders
from PythonProject2.src.item_models.data_model_items import AuthData,RequestItem
from PythonProject2.src.item_models.data_model_items import RequestItem
import allure
import requests
import json

class ItemsApi:
    def __init__(self,item_session):
       self.session = item_session
       self.base_url = ConstURL.ITEMS_URL.value
       self.headers = ApiHeaders.API_HEADERS.value
       self.token =  AuthData().auth_token()
       self.data_generator = RequestItem

    def get_all_items(self):
        """Запрос на получение списка всех items"""
        token_item = self.token
        params = {'skip': 0, 'limit': 100}
        response = self.session.get(f'{self.base_url}', params=params,
                                    headers=token_item.headers)
        if response.status_code != 200:
            response.raise_for_status()
        all_items = response.json()
        return all_items

class ItemScenarios:
    def __init__(self, token_session, api_client: ItemsApi):
        self.token_session = token_session
        self.api_client = api_client
        self.generate_dates = RequestItem

    def create_check_in_all_items(self):
        """
        Сценарий: создание итем, затем проверка наличия
        созданного итем в общем списке
        """
        # 1. Creating item
        item_create = self.api_client.create_item()
        id_item = item_create.get("id")
        print("Создан item =", id_item)
        print(item_create)

        #2 Get items
        items = self.api_client.get_all_items()
        assert len(items) > 0, "Получен пустой объект"  #
        print(f"Получен список всех items {items}")
        assert len(items.get("data")) == items.get("count"), "Несоответствие количества data и count" # LOOK перенести ассерты в тесты
        assert len(items.get("data")) and items.get("count") != 0, "Полученный объект пуст"
        print (f'data={len(items.get("data"))} должно быть равно count={items.get("count")}')
        assert item_create in items['data'], "созданного item нет в общем списке"
        return items


    def create_item(self):
        """Запрос на создание item"""
        with allure.step("Генерация данных для создания item"):
            item_create = self.data_generator

        with allure.step("Отправка POST-запроса на создание item"):
            response = self.session.post(f'{self.base_url}{self.items}',
                                         headers=self.headers, data=item_create)

        with allure.step("Проверка ответа"):
            if response.status_code != 200:
                allure.attach(body=response.text, name="Response error", attachment_type=allure.attachment_type.TEXT)
                response.raise_for_status()

        with allure.step("Получение JSON-ответа"):
            item_response = response.json()
            allure.attach(body=str(item_response), name="Response JSON", attachment_type=allure.attachment_type.JSON)

        return item_response

    @allure.title("Создание нового item")
    def create_item (self):
        """Запрос на создание item"""
        token_item = self.token
        item_create = self.data_generator.item_data()
        response = self.session.post(f'{self.base_url}',
                                     headers=token_item.headers,
                                     json=item_create)
        allure.attach(str(response), name="Результат запроса на создание item", attachment_type=allure.attachment_type.TEXT)
        if response.status_code != 200:
            response.raise_for_status()
        item_response = response.json()
        print(f'token_item= {token_item.headers}')
        return item_response