class Urls:
    BASE_URL = "https://qa-scooter.praktikum-services.ru"

    # Courier endpoints
    CREATE_COURIER = f"{BASE_URL}/api/v1/courier"
    LOGIN_COURIER = f"{BASE_URL}/api/v1/courier/login"
    DELETE_COURIER = f"{BASE_URL}/api/v1/courier/"
    COURIER_ORDERS_COUNT = f"{BASE_URL}/api/v1/courier/"

    # Orders endpoints
    CREATE_ORDER = f"{BASE_URL}/api/v1/orders"
    GET_ORDER_LIST = f"{BASE_URL}/api/v1/orders"
    GET_ORDER_BY_TRACK = f"{BASE_URL}/api/v1/orders/track"
    ACCEPT_ORDER = f"{BASE_URL}/api/v1/orders/accept/"
    FINISH_ORDER = f"{BASE_URL}/api/v1/orders/finish/"
    CANCEL_ORDER = f"{BASE_URL}/api/v1/orders/cancel"

    # Utils endpoints
    PING = f"{BASE_URL}/api/v1/ping"
    SEARCH_STATIONS = f"{BASE_URL}/api/v1/stations/search"
