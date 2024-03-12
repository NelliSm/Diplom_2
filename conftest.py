import pytest
import requests
import random
from data import DataUrl


#фикстура авторизации конкретного пользователя
@pytest.fixture
def login_user():
    payload = {"email": "nellySm@yandex.ru",
               "password": "NellyStBur",
               "name": "NellySmet"}
    response = requests.post(DataUrl.url + DataUrl.login, data=payload).json()
    token = response.get('accessToken')
    return token


#фикстура возвращает токен зарегистрированного пользователя(рандомного)
@pytest.fixture
def reg_random_user():
    payload = {"email": f"kek{random.randint(1, 9999)}@yang.ru",
               "password": f"pass{random.randint(1, 9999)}",
               "name": f"names{random.randint(1, 9999)}"}
    response = requests.post(DataUrl.url + DataUrl.register, json=payload)
    answer = response.json()
    access_token = answer.get('accessToken')
    return access_token


#фикстура возвращает список id полученых ингредиентов для создания заказа
@pytest.fixture
def get_ingredients():
    response = requests.get(DataUrl.url + DataUrl.ingredients)
    return [ingredient["_id"] for ingredient in response.json()["data"]]
