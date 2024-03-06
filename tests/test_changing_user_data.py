import pytest
import requests
import random
import allure
from data import DataUrl


class TestChangeUser:

    @allure.title('Изменение данных пользователя с различными сценариями')
    @allure.description('Попытка изменить данные профиля когда пользователь не авторизован')
    def test_changing_authorization_user(self):
        new_payload = {
            "email": "oonellySm@yandex.ru",
            "password": "ooNellyStBur",
            "name": "ooNellySmet"
        }
        response = requests.patch(DataUrl.url + DataUrl.change, data=new_payload)
        assert response.status_code == 401
        assert response.text == '{"success":false,"message":"You should be authorised"}'
        print(response.text)

    @allure.description('Попытка изменить данные профиля когда пользователь авторизован')
    def test_token_access(self, reg_random_user):
        headers = {'Authorization': reg_random_user}
        payload = {"email": f"k{random.randint(1, 9999)}@ya.ru",
                   "password": f"p{random.randint(1, 9999)}",
                   "name": f"gomer{random.randint(1, 9999)}"
                   }
        response = requests.patch(DataUrl.url + DataUrl.change,
                                  headers=headers, json=payload)
        assert "user" in response.text
        print(response.text)
