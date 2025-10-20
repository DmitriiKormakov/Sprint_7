# Тестирование API Яндекс Самокат

Проект автоматизированного тестирования API сервиса Яндекс Самокат.

## Структура проекта

QA_SPRINT_7/
├── helpers/ # Вспомогательные модули
│ ├── urls.py # URL эндпоинтов API
│ ├── api_client.py # Клиент для работы с API
│ ├── data.py # Генерация тестовых данных
│ └── messages.py # Сообщения об ошибках
├── tests/ # Тесты
│ ├── test_courier.py # Тесты курьеров
│ ├── test_orders.py # Тесты заказов
│ ├── test_utils.py # Тесты утилит
│ ├── test_additional.py # Дополнительные тесты
│ └── conftest.py # Фикстуры pytest
├── allure-results/ # Результаты для Allure-отчетов
├── requirements.txt # Зависимости проекта
└── README.md # Документация

## Установка и запуск

1. **Установите зависимости:**
pip install -r requirements.txt

2. **Запустите тесты:**
# Все тесты
pytest --alluredir=allure-results

# Конкретный тест
pytest tests/test_courier.py -v

3. **Просмотрите отчет Allure:**
allure serve allure-results

Тестируемые эндпоинты

Основное задание
✅ POST /api/v1/courier - Создание курьера

✅ POST /api/v1/courier/login - Логин курьера

✅ POST /api/v1/orders - Создание заказа

✅ GET /api/v1/orders - Список заказов

Дополнительное задание
✅ DELETE /api/v1/courier/{id} - Удаление курьера

✅ PUT /api/v1/orders/accept/{id} - Принятие заказа

✅ GET /api/v1/orders/track - Получение заказа по номеру

