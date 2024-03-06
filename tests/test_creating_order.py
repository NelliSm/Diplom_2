import requests
import random
import allure
from data import DataUrl


class TestOrder:

    @allure.title('Создание заказа с различными параметрами')
    @allure.description('Создание заказа без авторизации пользователя. '
                        'В payload берем первый ингредиент из списка, который возвращает фикстура')
    def test_make_order_from_single_ingredient(self, get_ingredients):
        payload = {"ingredients": [get_ingredients[0]]}
        response = requests.post(DataUrl.url + DataUrl.orders, json=payload)
        assert response.status_code == 200
        assert "number" in response.text
        print(response.json())

    @allure.description('Создание заказа без авторизации пользователя. '
                        'В payload берем два рандомных ингредиента из списка, который возвращает фикстура')
    def test_make_order_from_two_random_ingredients(self, get_ingredients):
        payload = {"ingredients": random.sample(get_ingredients, 2)}
        response = requests.post(DataUrl.url + DataUrl.orders, json=payload)
        assert response.status_code == 200
        assert "number" in response.text
        print(response.json())

    @allure.description('Попытка создать заказ с пустым списком ингредиентов')
    def test_make_order_without_ingredients(self):
        payload = {"ingredients": []}
        response = requests.post(DataUrl.url + DataUrl.orders, json=payload)
        assert response.status_code == 400
        assert response.text == '{"success":false,"message":"Ingredient ids must be provided"}'
        print(response.json())

    @allure.description('Попытка создать заказ с неверным хешем ингредиентов')
    def test_make_order_invalid_ingredients(self):
        payload = {"ingredients": ['61c0c', '61c0c5a']}
        response = requests.post(DataUrl.url + DataUrl.orders, json=payload)
        assert response.status_code == 500
        assert "Internal Server Error" in response.text
        print(response.text)

    @allure.description('Создание заказа авторизованным пользователем. Используются две фикстуры. '
                        'Первая создает пользователя, вторая отдает список ингридиентов для заказа')
    def test_make_order_authorization_user(self, reg_random_user, get_ingredients):
        payload = {"ingredients": [get_ingredients[0]]}
        response = requests.post(DataUrl.url + DataUrl.orders, headers={'Authorization': reg_random_user}, json=payload)
        assert response.status_code == 200
        assert "number" in response.text
        print(response.json())

    @allure.description('Создание заказа авторизованным пользователем. Используются две фикстуры. '
                        'Первая отдает токен пользователя, вторая отдает список ингридиентов для заказа')
    def test_make_order_authorization_user(self, login_user, get_ingredients):
        payload = {"ingredients": random.sample(get_ingredients, 2)}
        response = requests.post(DataUrl.url + DataUrl.orders, headers={'Authorization': login_user}, json=payload)
        assert response.status_code == 200
        assert "number" in response.text
        print(login_user)
        print(response.json())
