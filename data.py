import pytest
import requests


class DataUrl:
    url = 'https://stellarburgers.nomoreparties.site'
    register = '/api/auth/register'
    login = '/api/auth/login'
    orders = '/api/orders'
    change = '/api/auth/user'
    ingredients = '/api/ingredients'


class ConstantsData:
    NAME = 'nelly'
    LOGIN_EMAIL = 'nelly4777@yandex.ru'
    LOGIN_PASSWORD = '654123'


#фикстура содания конкретного пользователя
@pytest.fixture
def creating_user():
    payload = {"email": "nellySm@yandex.ru",
               "password": "NellyStBur",
               "name": "NellySmet"}
    response = requests.post(DataUrl.url + DataUrl.register, json=payload)
    return response
