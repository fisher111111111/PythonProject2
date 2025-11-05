from PythonProject2.venv.src.enums.const_url import ConstURL, ApiHeaders
from PythonProject2.venv.src.data_models.data_model_items import AuthData,RequestItem
import requests
import json


class ItemsApi:
    def __init__(self,item_session):
       self.session = item_session
       self.base_url = ConstURL.ITEMS_URL.value
       self.headers = ApiHeaders.API_HEADERS.value
       self.token =  AuthData().auth_token()
       self.data_generator = RequestItem

    def create_item (self):
        """Запрос на создание item"""
        token_item = self.token
        item_create = self.data_generator.item_data()
        response = self.session.post(f'{self.base_url}',
                                     headers=token_item.headers,
                                     json=item_create)
        if response.status_code != 200:
            response.raise_for_status()
        item_response = response.json()
        return item_response

# if __name__ == '__main__':
#     item_session = requests.Session()
#     api = ItemsApi(item_session)
#     result = api.create_item()
#     print(result)

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
#
# if __name__ == '__main__':
#     item_session = requests.Session()
#     api = ItemsApi(item_session)
#     result = api.get_all_items()
#     for item in result['data']:  # Цикл по result['data'] выводит каждый объект отдельно на новой строке.
#         print(json.dumps(item, ensure_ascii=False, indent=0)) #- json.dumps() форматирует словарь
#                                                               # в строку JSON с отступами и без
#                                                               # экранирования кириллицы (ensure_ascii=False)
#                                                               # indent=4 -каждый уровень вложенности будет отступать на 4 пробела.
#         print()  #  после каждого объекта создаёт пустую строку для удобочитаемости

    def get_item (self, item_id):
        token_item = self.token
        response = self.session.get(f'{self.base_url}{item_id}',
                                    headers=token_item.headers)
        if response.status_code != 200:
            response.raise_for_status()
        item = response.json()
        return item


# if __name__ == '__main__':
#     item_session = requests.Session()
#     api = ItemsApi(item_session)
#
#     # Создаем новую запись
#     created_item = api.create_item()
#     print('Созданная запись:', created_item)
#
#     # Получаем id созданной записи
#     item_id = created_item['id']
#
#     # Делаем GET-запрос по этому id, чтобы получить запись с сервера
#     item_by_id = api.get_item(item_id)
#     print('Запись, полученная по id:', item_by_id)

    def update_item (self, item_id):
        """Запрос на обновление item"""
        token_item = self.token
        item_update = self.data_generator.update_item_data()
        response = self.session.put(f'{self.base_url}{item_id}',
                                     headers=token_item.headers,
                                     json=item_update)
        if response.status_code != 200:
            response.raise_for_status()
        item_response = response.json()
        return item_response

# if __name__ == '__main__':
#     item_session = requests.Session()
#     api = ItemsApi(item_session)
#     # Создаем новую запись
#     created_item = api.create_item()
#     print('Созданная запись:', created_item)
#     # Получаем id созданной записи
#     item_id = created_item['id']
#     # Делаем PUT-запрос по этому id, чтобы изменить запись с сервера
#     item_by_id = api.update_item(item_id)
#     print('Измененная запись',item_by_id)

    def delete_item (self, item_id):
        token_item = self.token
        response = self.session.delete(f'{self.base_url}{item_id}',
                                    headers=token_item.headers)
        if response.status_code != 200:
            response.raise_for_status()
        item_response = response.text
        return item_response

# if __name__ == '__main__':
#     item_session = requests.Session()
#     api = ItemsApi(item_session)
#     # Создаем новую запись
#     created_item = api.create_item()
#     print('Созданная запись:', created_item)
#     # Получаем id созданной записи
#     item_id = created_item['id']
#     # Делаем DEL-запрос по этому id, чтобы удалить запись с сервера
#     item_by_id = api.delete_item(item_id)
#     print('Удаленная запись',item_by_id)