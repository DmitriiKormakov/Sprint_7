import allure
import pytest
import random
import string
from helpers.messages import Messages


def generate_random_string(length):
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


class TestCourierCreation:
    @allure.title("Успешное создание курьера")
    def test_create_courier_success(self, api_client):
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        response = api_client.create_courier(login, password, first_name)
        assert response.status_code == 201
        assert response.json()["ok"] == True

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier_fails(self, api_client):
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        api_client.create_courier(login, password, first_name)
        response = api_client.create_courier(login, password, first_name)

        assert response.status_code == 409
        response_data = response.json()
        assert response_data["code"] == 409
        assert (
            response_data["message"]
            == "Этот логин уже используется. Попробуйте другой."
        )

    @allure.title("Создание курьера без логина")
    def test_create_courier_without_login_fails(self, api_client):
        response = api_client.create_courier("", "password", "name")
        assert response.status_code == 400
        response_data = response.json()
        assert response_data["code"] == 400
        assert response_data["message"] == Messages.NOT_ENOUGH_DATA_FOR_CREATE

    @allure.title("Создание курьера без пароля")
    def test_create_courier_without_password_fails(self, api_client):
        response = api_client.create_courier("login", "", "name")
        assert response.status_code == 400
        response_data = response.json()
        assert response_data["code"] == 400
        assert response_data["message"] == Messages.NOT_ENOUGH_DATA_FOR_CREATE


class TestCourierLogin:
    @allure.title("Успешный логин курьера")
    def test_login_courier_success(self, api_client):
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        api_client.create_courier(login, password, first_name)
        response = api_client.login_courier(login, password)

        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Логин с неверным паролем")
    def test_login_courier_wrong_password(self, api_client):
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        api_client.create_courier(login, password, first_name)
        response = api_client.login_courier(login, "wrong_password")

        assert response.status_code == 404
        response_data = response.json()
        assert response_data["code"] == 404
        assert response_data["message"] == Messages.ACCOUNT_NOT_FOUND

    @allure.title("Логин без пароля")
    def test_login_courier_without_password(self, api_client):
        response = api_client.login_courier("login", "")
        assert response.status_code == 400
        response_data = response.json()
        assert response_data["code"] == 400
        assert response_data["message"] == Messages.NOT_ENOUGH_DATA_FOR_LOGIN

    @allure.title("Логин без логина")
    def test_login_courier_without_login(self, api_client):
        response = api_client.login_courier("", "password")
        assert response.status_code == 400
        response_data = response.json()
        assert response_data["code"] == 400
        assert response_data["message"] == Messages.NOT_ENOUGH_DATA_FOR_LOGIN

    @allure.title("Логин несуществующего курьера")
    def test_login_nonexistent_courier(self, api_client):
        response = api_client.login_courier("nonexistent", "password")

        # Сервер автоматически создает нового курьера при логине несуществующего
        assert response.status_code == 200
        assert "id" in response.json()
        courier_id = response.json()["id"]
        assert isinstance(courier_id, int)
