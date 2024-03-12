import requests
import random
import allure
from data import DataUrl


@allure.suite('Логин пользователя с разными сценариями')
class TestLoginUser:

    @allure.description('Авторизация под существующим пользователем из фикстуры создания пользователя')
    def test_login_existing_user(self):
        payload = {
            "email": "nellySm@yandex.ru",
            "password": "NellyStBur",
            "name": "NellySmet"}
        response = requests.post(DataUrl.url + DataUrl.login, json=payload)
        assert response.status_code == 200
        assert '"success":true' in response.text

    @allure.description('Авторизация под неверным логином и паролем')
    def test_login_user_error(self):
        payload = {
            "email": f"ku{random.randint(1, 999)}@ya.ru",
            "password": f"pass{random.randint(1, 999)}",
        }
        response = requests.post(DataUrl.url + DataUrl.login, json=payload)
        assert response.status_code == 401
        assert response.text == '{"success":false,"message":"email or password are incorrect"}'
