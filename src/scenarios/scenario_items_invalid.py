from PythonProject2.src.enums.const_url import ConstURL, ApiHeaders
from PythonProject2.src.data_models.data_model_items import AuthData,RequestItem, WrongItems, NoneItems
from PythonProject2.src.api.api_items import ItemsApi
import requests
import json

class BadScenarioCreate:
    def __init__(self,item_session):
        self.session = item_session
        self.base_url = ConstURL.ITEMS_URL.value
        self.token =  AuthData().auth_token()
        self.data_generator = RequestItem
        self.wrong_data = WrongItems
        self.non_data = NoneItems

    def create_too_long_title (self):
        """Запрос на создание item"""
        token_item = self.token
        item_create = self.wrong_data.too_long_data()
        response = self.session.post(f'{self.base_url}',
                                     headers=token_item.headers,
                                     json=item_create)
        item_response = response.text
        print(response.text)
        return item_response

# if __name__ == "__main__":
#     item_session = requests.Session()
#     api = BadScenarioCreate(item_session)
#     result = api.create_too_long_title()
#     print(f' wrong_title result = {result}')

    def create_non_title(self):
        """Запрос на создание item"""
        token_item = self.token
        item_create = self.non_data.none_item_data()
        response = self.session.post(f'{self.base_url}',
                                     headers=token_item.headers,
                                     json=item_create)
        item_response = response.text
        return item_response

# if __name__ == "__main__":
#     item_session = requests.Session()
#     api = BadScenarioCreate(item_session)
#     result = api.create_non_title()
#     print(f' non_title result = {result}')

    def create_empty_token(self):
        """Запрос на создание item"""
        token_item = self.token
        token_item.headers['Authorization'] = None
        item_create = self.wrong_data.too_long_data()
        response = self.session.post(f'{self.base_url}',
                                     headers=token_item.headers,
                                     json=item_create)
        item_response = response.text
        print(token_item.headers)
        print(response.text, response.status_code)
        return item_response

# if __name__ == "__main__":
#     item_session = requests.Session()
#     api = BadScenarioCreate(item_session)
#     result = api.create_empty_token()
#     print(f' wrong_title result = {result}')

class BadScenariosItem:
    def __init__(self, item_session, api_client: ItemsApi):
        self.session = item_session
        self.api_client = api_client
        self.generate_dates = RequestItem
        self.base_url = ConstURL.ITEMS_URL.value
        self.token =  AuthData().auth_token()
        self.empty_token = AuthData().auth_empty_token()

    def create_and_get_empty_token(self):
        '''
        Сценарий: создание итем, проверка ID созданного итем,
        затем удаление этого итем '''
        # 1. Creating item
        item_create= self.api_client.create_item()
        id_item = item_create.get("id")
        print("Создан item =", id_item)

        #2 Get item with empty token
        empty_token = self.empty_token
        response = self.session.get(f'{self.base_url}{id_item}',
                                    headers=empty_token.headers)
        item = response.json()
        return item

# if __name__ == "__main__":
#     # Инициализируем необходимые объекты
#     item_session = requests.Session()  # здесь создайте или получите сессию с токеном
#     api_client = ItemsApi(item_session)  # инициализация API клиента с нужными параметрами
#     # Создаем объект класса
#     scenarios = BadScenariosItem(item_session, api_client)
#     # Вызываем метод
#     item_id = scenarios.create_and_get_empty_token()
#     print(f"Обработанный item ID: {item_id}")

    def create_and_update_empty_token(self):
        '''
        Сценарий: создание итем, проверка ID созданного итем,
        затем удаление этого итем '''
        # 1. Creating item
        item_create= self.api_client.create_item()
        id_item = item_create.get("id")
        print("Создан item =", id_item)

        #2 Update item with empty token
        empty_token = self.empty_token
        item_update = self.generate_dates.update_item_data()
        response = self.session.put(f'{self.base_url}{id_item}',
                                     headers=empty_token.headers,
                                     json=item_update)
        item = response.json()
        return item

# if __name__ == "__main__":
#     # Инициализируем необходимые объекты
#     item_session = requests.Session()  # здесь создайте или получите сессию с токеном
#     api_client = ItemsApi(item_session)  # инициализация API клиента с нужными параметрами
#     # Создаем объект класса
#     scenarios = BadScenariosItem(item_session, api_client)
#     # Вызываем метод
#     item_id = scenarios.create_and_update_empty_token()
#     print(f"Обработанный item ID: {item_id}")

    def create_and_delete_empty_token(self):
        '''
        Сценарий: создание итем, проверка ID созданного итем,
        затем удаление этого итем '''
        # 1. Creating item
        item_create= self.api_client.create_item()
        id_item = item_create.get("id")
        print("Создан item =", id_item)

        #2 Delete item with empty token
        empty_token = self.empty_token
        response = self.session.delete(f'{self.base_url}{id_item}',
                                       headers=empty_token.headers)
        item_response = response.text
        return item_response

# if __name__ == "__main__":
#     # Инициализируем необходимые объекты
#     item_session = requests.Session()  # здесь создайте или получите сессию с токеном
#     api_client = ItemsApi(item_session)  # инициализация API клиента с нужными параметрами
#     # Создаем объект класса
#     scenarios = BadScenariosItem(item_session, api_client)
#     # Вызываем метод
#     item_id = scenarios.create_and_delete_empty_token()
#     print(f"Обработанный item ID: {item_id}")