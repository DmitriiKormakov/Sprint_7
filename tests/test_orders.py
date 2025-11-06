import allure
import pytest


class TestOrderCreation:
    @pytest.mark.parametrize("color", [
        ["BLACK"],
        ["GREY"], 
        ["BLACK", "GREY"],
        []
    ])
    @allure.title("Создание заказа с цветом: {color}")
    def test_create_order_with_different_colors(self, api_client, color):
        order_data = {
            "firstName": "Naruto",
            "lastName": "Uzumaki",
            "address": "Konoha, 142 apt.",
            "metroStation": "4",
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2024-12-12",
            "comment": "Saske, come back to Konoha",
            "color": color
        }
        
        response = api_client.create_order(order_data)
        assert response.status_code == 201
        response_data = response.json()
        assert "track" in response_data
        assert isinstance(response_data["track"], int)


class TestOrdersList:
    @allure.title("Получение списка заказов")
    def test_get_orders_list_returns_orders(self, api_client):
        response = api_client.get_orders_list(limit=5)
        assert response.status_code == 200
        response_data = response.json()
        assert "orders" in response_data
        assert isinstance(response.json()["orders"], list)