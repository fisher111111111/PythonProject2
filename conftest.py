import pytest
import requests
import allure
from PythonProject2.src.utils_item.urls_item import ItemsURLs
from PythonProject2.src.item_models.data_model_items import RequestItem, WrongItems, NoneItems,ResponseItem, ResponseUserItems, AuthData

BASE_URL = ItemsURLs.base_url()
ITEMS = ItemsURLs.items_endpoint()
LOGIN = ItemsURLs.auth_endpoint()


"""Фикстуры для позитивных тестов"""
@pytest.fixture(scope="session")
@allure.title("Фикстура генерации тестовых данных для создания item")
def create_item_data():
    data_item = RequestItem.item_data()
    return data_item

@pytest.fixture(scope="session")
@allure.title("Фикстура генерации тестовых данных для обновления item")
def upd_item_data():
    upd_item = RequestItem.update_item_data
    return upd_item

@pytest.fixture(scope="session")
@allure.title("Фикстура генерации недефолтных параметров для GET всех items")
def params_get_items():
    params_items = RequestItem.params_valid
    return params_items

@pytest.fixture(scope="session")
@allure.title("Фикстура для получения ID созданного item")
def take_id_item(item_token,create_item_data):
    with allure.step("Отправляем POST запрос на создание item"):
        response = requests.post(ITEMS,
                                 headers=item_token.headers,
                                 json=create_item_data)
        allure.attach(str(response), name="Результат запрос на создание item",
                      attachment_type=allure.attachment_type.JSON)
        assert response.status_code == 200, "Неудачное создание item"
    with allure.step("Забираем ID полученного item"):
        id_item = response.json()["id"]
        allure.attach(str(id_item), name="ID полученного item", attachment_type=allure.attachment_type.TEXT)
        assert response.status_code == 200
        return id_item

@pytest.fixture(scope="session")
@allure.title("Фикстура для удаления полученного item")
def del_item(take_id_item, item_token):
    with allure.step("Вновь берем полученный item для его удаления"):
        yield take_id_item
        allure.attach(str(take_id_item), name="Результат работы yield", attachment_type=allure.attachment_type.TEXT)
    with allure.step("Отправляем DELETE запрос на удаление item"):
        response = requests.delete(ITEMS,
                                   params=take_id_item,
                                   headers=item_token.headers)
        allure.attach(str(response), name="Результат запроса на удаление", attachment_type=allure.attachment_type.TEXT)
        assert response.status_code == 200, "Неудачная работа фикстуры по удалению items"
        return response.text

"""Фикстуры для негативных тестов"""
@pytest.fixture(scope="session")
@allure.title("Фикстура для генерации данных title > 256 символов")
def over_long_title():
    long_title = WrongItems.too_long_data
    return long_title

@pytest.fixture(scope="session")
@allure.title("Фикстура для получения пустого значения для title")
def empty_title():
    empty_data_title = NoneItems.none_item_data
    return empty_data_title

"""Фикстуры для тестирования токена и авторизации"""
@pytest.fixture(scope="session")
@allure.title("Фиктура для получения токена")
def item_token():
    data_token = AuthData.auth_token
    return data_token

@pytest.fixture(scope="session")
@allure.title("Фикстура для получения пустого токена")
def empty_token():
    empty_token_data = AuthData.auth_empty_token
    return empty_token_data