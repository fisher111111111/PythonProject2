import pytest
import requests
import allure
from PythonProject2.src.item_models.data_model_items import RequestItem, WrongRequestItems, NoneItems,ResponseItem, ResponseAllItems, AuthData
from PythonProject2.src.utils_item.urls_item import ItemsURLs
from PythonProject2.src.api.api_items import ItemsApi
from PythonProject2.src.scenarios.scenario_items_valid import ItemScenarios
from PythonProject2.src.scenarios.scenario_items_invalid import BadScenariosItem, BadScenarioCreate
from PythonProject2.src.api.login_access import AuthLogin

BASE_URL = ItemsURLs.base_url()
ITEMS = ItemsURLs.items_endpoint()
ITEM = ItemsURLs.items_endpoint_id
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
    upd_item = RequestItem.update_item_data()
    return upd_item

@pytest.fixture(scope="session")
@allure.title("Фикстура генерации недефолтных параметров для GET всех items")
def params_get_items():
    params_items = RequestItem.params_valid
    return params_items

@pytest.fixture(scope="session")
@allure.title("Фикстура для получения ID созданного item")
def take_id_item(item_token, create_item_data):
    with allure.step("Отправляем POST запрос на создание item"):
        response = requests.post(ITEMS,
                                 headers=item_token,
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
def deleting_item(take_id_item, item_token):
    with allure.step("Вновь берем полученный item для его удаления"):
        yield take_id_item
        allure.attach(str(take_id_item), name="Результат работы yield", attachment_type=allure.attachment_type.TEXT)
    with allure.step("Отправляем DELETE запрос на удаление item"):
        response = requests.delete(ITEM(take_id_item),
                                   headers=item_token)
        allure.attach(str(response), name="Результат запроса на удаление", attachment_type=allure.attachment_type.TEXT)
    assert response.status_code == 200, "Неудачная работа фикстуры по удалению items"
    return response.text

@pytest.fixture(scope="session")
@allure.title("Фикстура для удаления полученного item")
def del_item(item_token, create_item_data):
    with allure.step("Отправляем POST запрос на создание item"):
        response = requests.post(ITEMS,
                                 headers=item_token,
                                 json=create_item_data)
        allure.attach(str(response), name="Результат запрос на создание item",
                      attachment_type=allure.attachment_type.JSON)
    assert response.status_code == 200, "Неудачное создание item"
    with allure.step("Забираем ID полученного item"):
        id_item = response.json()["id"]
        allure.attach(str(id_item), name="ID полученного item", attachment_type=allure.attachment_type.TEXT)
    assert response.status_code == 200
    with allure.step("Вновь берем полученный item для его удаления"):
        yield id_item
        allure.attach(str(id_item), name="Результат работы yield", attachment_type=allure.attachment_type.TEXT)
    with allure.step("Отправляем DELETE запрос на удаление item"):
        response = requests.delete(ITEM(id_item),
                                   headers=item_token)
        allure.attach(str(response), name="Результат запроса на удаление", attachment_type=allure.attachment_type.TEXT)
    assert response.status_code == 200, "Неудачная работа фикстуры по удалению items"
    return response.text

"""Фикстуры для негативных тестов"""

@pytest.fixture(scope="session")
@allure.title("Фикстура для генерации данных title > 256 символов")
def over_long_title():
    long_title = WrongRequestItems.too_long_data()
    return long_title

@pytest.fixture(scope="session")
@allure.title("Фикстура для получения пустого значения для title")
def empty_title():
    empty_data_title = NoneItems.none_item_data()
    return empty_data_title

"""Фикстуры для тестирования токена и авторизации"""
@pytest.fixture(scope="session")
@allure.title("Фикстура для получения сессии")
def item_session():
    with allure.step("Получаем объект сессии item"):
        data_session = AuthData.auth_token()
        allure.attach(str(data_session), name="Результат получения объекта сессии item",
                      attachment_type=allure.attachment_type.TEXT)
    return data_session

@pytest.fixture(scope="session")
@allure.title("Фикстура для получения header с валидным токеном")
def item_token():
    with allure.step("Получаем headers c валидным токеном"):
        data_token = dict(AuthData().auth_token().headers)
        allure.attach(str(data_token), name="Результат полученных headers с валидным токеном",
                      attachment_type=allure.attachment_type.JSON)
    return data_token

# a = item_token()
# print (f"item_token -> {a}")

@pytest.fixture(scope="session")
@allure.title("Фикстура для получения пустого токена")
def empty_token():
    with allure.step("Получаем headers с пустым токеном"):
        empty_token_data = dict(AuthData().empty_token().headers)
        allure.attach(str(empty_token_data), name="Результат получения headers с пустым токеном", attachment_type=allure.attachment_type.JSON)
    return empty_token_data

"""Фикстура для обработки объектов логина"""
@pytest.fixture(scope="session")
def login_scenarios():
    session = requests.Session()
    api_login = AuthLogin(session)
    return api_login

"""Фикстура для создания объекта класса сценария"""
@pytest.fixture(scope="session")
def valid_scenarios():
    session = requests.Session()
    api_client = ItemsApi(session)
    scenarios = ItemScenarios(session, api_client)
    return scenarios

@pytest.fixture(scope="session")
def invalid_create():
    session = requests.Session()
    scenarios = BadScenarioCreate(session)
    return scenarios

@pytest.fixture(scope="session")
def invalid_item():
    session = requests.Session()
    api_client = ItemsApi(session)
    scenarios = BadScenariosItem(session, api_client)
    return scenarios

@pytest.fixture(scope="session")
def cleanup_items():
    session = requests.Session()
    api_client = ItemsApi(session)
    item_ids = []

    yield item_ids  # тест добавляет id сюда

    # после теста удаляем все item по id
    for item_id in item_ids:
        delete_response =api_client.delete_item(item_id)
        assert delete_response.status_code == 200
