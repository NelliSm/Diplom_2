import requests
import allure
from data import DataUrl


@allure.suite('Получение заказов конкретного пользователя')
class TestGetOrder:

    @allure.description('Получение списка заказов авторизованного пользователя')
    def test_get_orders_authorization_user(self, login_user):
        response = requests.get(DataUrl.url + DataUrl.orders, headers={'authorization': login_user})
        assert response.status_code == 200
        assert 'orders' in response.text

    @allure.description('Получение списка заказов неавторизованным пользователем')
    def test_get_orders_not_authorization_user(self):
        response = requests.get(DataUrl.url + DataUrl.orders)
        assert response.status_code == 401
        assert response.text == '{"success":false,"message":"You should be authorised"}'
