import requests
from PythonProject2.src.api.api_items import ItemsApi
from PythonProject2.src.data_models.data_model_items import RequestItem


class ItemScenarios:
    def __init__(self, token_session, api_client: ItemsApi):
        self.token_session = token_session
        self.api_client = api_client
        self.generate_dates = RequestItem

    def create_check_delete_item(self):
        '''
        Сценарий: создание итем, проверка ID созданного итем,
        затем удаление этого итем '''
        # 1. Creating item
        item_create= self.api_client.create_item()
        id_item = item_create.get("id")
        print("Создан item =", id_item)

        #2 Check item creating
        if id_item is None:
            raise RuntimeError ("Не удачное получение созданного item")
        print("Успешная проверка item")

        #3 Deleting item
        self.api_client.delete_item(id_item)
        print(f'item c ID {id_item} успешно удален')
        return id_item

# if __name__ == "__main__":
#     # Инициализируем необходимые объекты
#     token_session = requests.Session()  # здесь создайте или получите сессию с токеном
#     api_client = ItemsApi(token_session)  # инициализация API клиента с нужными параметрами
#     # Создаем объект класса
#     scenarios = ItemScenarios(token_session, api_client)
#     # Вызываем метод
#     item_id = scenarios.create_check_delete_item()
#     print(f"Обработанный item ID: {item_id}")

    def create_check_update_item(self):
        '''
        Сценарий: создание итем, проверка ID созданного итем,
        затем обновление итем '''
        # 1. Creating item
        item_create = self.api_client.create_item()
        id_item = item_create.get("id")
        print("Создан item =", id_item)
        print(item_create)

        #2 Check item creating
        if id_item is None:
            raise RuntimeError ("Не удачное получение созданного item")
        print("Успешная проверка item")

        #3 Updating item
        # upd_item_data = self.generate_dates.update_item_data()
        update_item = self.api_client.update_item(id_item)
        return update_item

# if __name__ == "__main__":
#     # Инициализируем необходимые объекты
#     token_session = requests.Session()  # здесь создайте или получите сессию с токеном
#     api_client = ItemsApi(token_session)  # инициализация API клиента с нужными параметрами
#     # Создаем объект класса
#     scenarios = ItemScenarios(token_session, api_client)
#     # Вызываем метод
#     item_id = scenarios.create_check_update_item()
#     print(f"Обработанный item ID: {item_id}")

    def create_check_get_item (self):
        '''
        Сценарий: Создание итем, проверка ID созданного итем,
        затем получение итем по ID
        '''
        # 1. Creating item
        item_create = self.api_client.create_item()
        id_item = item_create.get("id")
        print("Создан item =", id_item)
        print(item_create)

        #2 Check item creating
        if id_item is None:
            raise RuntimeError ("Не удачное получение созданного item")
        print("Успешная проверка item")

        #3 Get item
        get_item = self.api_client.get_item(id_item)
        assert item_create == get_item, "сравнение items провалено"
        print(get_item)
        return get_item

# if __name__ == "__main__":
#     # Инициализируем необходимые объекты
#     token_session = requests.Session()  # здесь создайте или получите сессию с токеном
#     api_client = ItemsApi(token_session)  # инициализация API клиента с нужными параметрами
#     # Создаем объект класса
#     scenarios = ItemScenarios(token_session, api_client)
#     # Вызываем метод
#     item_id = scenarios.create_check_get_item()
#     print(f"Обработанный item ID: {item_id}")

    def create_check_in_all_items(self):
        """
        Cwtyfhbq^ cоздание итем, затем проверка наличия
        созданного итем в общем списке
        """
        # 1. Creating item
        item_create = self.api_client.create_item()
        id_item = item_create.get("id")
        print("Создан item =", id_item)
        print(item_create)

        #2 Get items
        items = self.api_client.get_all_items()
        assert len(items) > 0, "Получен пустой объект"
        print(f"Получен список всех items {items}")
        assert len(items.get("data")) == items.get("count"), "Несоответствие количества data и count"
        assert len(items.get("data")) and items.get("count") != 0, "Полученный объект пуст"
        print (f'data={len(items.get("data"))} должно быть равно count={items.get("count")}')
        assert item_create in items['data'], "созданного item нет в общем списке"
        return items

if __name__ == "__main__":
    # Инициализируем необходимые объекты
    token_session = requests.Session()  # здесь создайте или получите сессию с токеном
    api_client = ItemsApi(token_session)  # инициализация API клиента с нужными параметрами
    # Создаем объект класса
    scenarios = ItemScenarios(token_session, api_client)
    # Вызываем метод
    item_id = scenarios.create_check_in_all_items()
