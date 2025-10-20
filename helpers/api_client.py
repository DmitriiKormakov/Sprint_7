import requests
import allure
from helpers.urls import Urls


class ScooterApiClient:
    
    @allure.step("Создать курьера")
    def create_courier(self, login, password, first_name):
        payload = {
            "login": login,
            "password": password, 
            "firstName": first_name
        }
        return requests.post(Urls.CREATE_COURIER, json=payload)
    
    @allure.step("Логин курьера")
    def login_courier(self, login, password):
        payload = {
            "login": login,
            "password": password
        }
        return requests.post(Urls.LOGIN_COURIER, json=payload)
    
    @allure.step("Удалить курьера")
    def delete_courier(self, courier_id):
        return requests.delete(Urls.DELETE_COURIER + str(courier_id))
    
    @allure.step("Создать заказ")
    def create_order(self, order_data):
        return requests.post(Urls.CREATE_ORDER, json=order_data)
    
    @allure.step("Получить список заказов")
    def get_orders_list(self, courier_id=None, limit=30, page=0):
        params = {
            "limit": limit,
            "page": page
        }
        if courier_id:
            params["courierId"] = courier_id
            
        return requests.get(Urls.GET_ORDER_LIST, params=params)
    
    @allure.step("Получить заказ по треку")
    def get_order_by_track(self, track):
        return requests.get(Urls.GET_ORDER_BY_TRACK, params={"t": track})
    
    @allure.step("Принять заказ")
    def accept_order(self, order_id, courier_id):
        params = {"courierId": courier_id}
        return requests.put(f"{Urls.ACCEPT_ORDER}{order_id}", params=params)
    
    @allure.step("Завершить заказ")
    def finish_order(self, order_id):
        return requests.put(f"{Urls.FINISH_ORDER}{order_id}")
    
    @allure.step("Отменить заказ")
    def cancel_order(self, track):
        payload = {"track": track}
        return requests.put(Urls.CANCEL_ORDER, json=payload)
    
    @allure.step("Получить количество заказов курьера")
    def get_courier_orders_count(self, courier_id):
        return requests.get(f"{Urls.COURIER_ORDERS_COUNT}{courier_id}/ordersCount")
    
    @allure.step("Поиск станций метро")
    def search_stations(self, search_string):
        return requests.get(Urls.SEARCH_STATIONS, params={"s": search_string})
    
    @allure.step("Проверить доступность сервера")
    def ping(self):
        return requests.get(Urls.PING)