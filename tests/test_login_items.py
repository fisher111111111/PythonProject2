import allure

from PythonProject2.src.item_models.data_model_items import ResponseLogin
from PythonProject2.src.utils_item.validator_item_data import validator_login


@allure.suite("Раздел Авторизация")
@allure.sub_suite("Позитивные сценарии")
class TestValidLogin:

    @allure.title("Тест на создание item")
    def test_create_token(self, login_scenarios):
        login = login_scenarios.create_token()
        login_json = login.json()
        validator_login(login, model=ResponseLogin, expected_data=login_json)
        data_access_token = login_json["access_token"]
        data_token_type = login_json["token_type"]
        assert login.status_code == 200, "Не ожидаемый статус-код"
        assert (
            isinstance(data_access_token, str) and data_access_token.count(".") == 2
        ), "Получен невалидный токен"
        assert len(data_access_token) == 165
        assert data_token_type == "bearer"
