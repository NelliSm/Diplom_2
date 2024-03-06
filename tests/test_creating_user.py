import pytest
import requests
import random
import allure
from data import DataUrl


class TestCreatingUser:

    @allure.title('Создание пользователя с различными сценариями')
    @allure.description('Создание уникального пользователя с рандомными валидными параметрами')
    def test_creating_new_user_success(self):
        payload = {
            "email": f"ku{random.randint(1, 100)}@mail.ru",
            "password": f"propass{random.randint(1, 100)}",
            "name": "Alex"
            }
        response = requests.post(DataUrl.url + DataUrl.register, json=payload)
        assert response.status_code == 200
        assert '"success":true' in response.text
        print(response.text)

    @allure.description('Попытка создать пользователя, который уже зарегистрирован посредством фмкстуры')
    def test_create_double_user_error(self, creating_user):
        payload = {"email": "nellySm@yandex.ru",
                   "password": "NellyStBur",
                   "name": "NellySmet"}
        response = requests.post(DataUrl.url + DataUrl.register, json=payload)
        assert response.status_code == 403
        assert response.text == '{"success":false,"message":"User already exists"}'
        print(response.text)

    @allure.description('Попытка создать пользователя без одного из обязательных параметров. '
                        'Используется параметризация с тремя наборами данных')
    @pytest.mark.parametrize('email, password, name', [
        ("Log@1.ru", "", "Alex"),
        ("", "Pass1602", "Alex"),
        ("Log@1.ru", "Pass1602", "")])
    def test_creating_user_missing_data_error(self, email, password, name):
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        response = requests.post(DataUrl.url + DataUrl.register, data=payload)
        assert response.status_code == 403
        assert response.text == '{"success":false,"message":"Email, password and name are required fields"}'
        print(response.json())
