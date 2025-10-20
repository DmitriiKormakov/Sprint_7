import allure


class TestUtils:
    @allure.title("Проверка доступности сервера")
    def test_ping_server(self, api_client):
        response = api_client.ping()
        assert response.status_code == 200
        assert response.text == "pong;"