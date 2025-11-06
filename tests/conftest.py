import pytest
from helpers.api_client import ScooterApiClient
from helpers.data import register_new_courier_and_return_login_password


@pytest.fixture
def api_client():
    """Фикстура для клиента API"""
    return ScooterApiClient()


@pytest.fixture
def random_courier():
    """Фикстура для создания случайного курьера"""
    return register_new_courier_and_return_login_password()


@pytest.fixture
def created_courier(api_client, random_courier):
    """Фикстура для создания и удаления курьера (уборка после тестов)"""
    login, password, first_name = random_courier
    # Создаем курьера
    api_client.create_courier(login, password, first_name)
    
    # Логинимся чтобы получить ID
    login_response = api_client.login_courier(login, password)
    courier_id = login_response.json()["id"]
    
    yield login, password, first_name, courier_id
    
    # Удаляем курьера после теста
    api_client.delete_courier(courier_id)