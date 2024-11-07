import os


class Config:
    # Путь к базе данных SQLite
    DATABASE_PATH = os.path.join(os.path.expanduser("~"), ".FinAnalytics", "database", "finance_tracker.db")

    # Использовать ли стиль (CSS файл)
    USE_STYLESHEET = True

    # Версия пакета
    __version__ = "1.0.0c"

    # Путь к файлу со стилями для PyQt (если используется)
    STYLESHEET_PATH = os.path.join(os.path.dirname(__file__), "resources", "styles.qss")

    # Настройки валюты
    DEFAULT_CURRENCY = "RUB"  # Валюта по умолчанию
    CURRENCY_SYMBOLS = {
        "USD": "$",
        "EUR": "€",
        "RUB": "₽",
    }

    # Настройки для отчетов
    REPORT_DEFAULT_PERIOD = "month"  # Период отчетов по умолчанию
    REPORT_PERIOD_OPTIONS = ["day", "week", "month", "year"]

    # Настройки для транзакций
    TRANSACTION_CATEGORIES = [
        "Еда", "Транспорт", "Коммунальные услуги", "Развлечения",
        "Здоровье", "Обучение", "Другое"
    ]
    DEFAULT_TRANSACTION_TYPE = "Расходы"  # Тип транзакции по умолчанию


# Проверка наличия папки для базы данных
db_directory = os.path.dirname(Config.DATABASE_PATH)
if not os.path.exists(db_directory):
    os.makedirs(db_directory)
