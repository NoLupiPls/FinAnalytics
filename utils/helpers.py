from PyQt5.QtCore import QDate
from datetime import datetime


def format_date(date_str):
    """
    Форматирует строку даты в стандартный формат 'YYYY-MM-DD'.

    :param date_str: Дата в формате строки (например, '2024-11-07').
    :return: Отформатированная строка даты.
    """
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime("%d %B %Y")
    except ValueError:
        return date_str  # Если формат даты некорректен, возвращаем исходную строку


def get_current_date():
    """
    Возвращает текущую дату в формате 'YYYY-MM-DD'.

    :return: Текущая дата в строковом формате.
    """
    return datetime.today().strftime("%Y-%m-%d")


def format_currency(amount):
    """
    Форматирует число как валюту с двумя знаками после запятой и разделением тысяч.

    :param amount: Сумма для форматирования.
    :return: Строка, представляющая отформатированную валюту.
    """
    try:
        return f"{amount:,.2f}"
    except (ValueError, TypeError):
        return str(amount)  # В случае ошибки просто возвращаем строку


def get_first_day_of_month(date_str):
    """
    Возвращает первый день месяца для заданной даты.

    :param date_str: Дата в формате 'YYYY-MM-DD'.
    :return: Дата первого дня месяца.
    """
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.replace(day=1).strftime("%Y-%m-%d")
    except ValueError:
        return date_str  # Если формат даты некорректен, возвращаем исходную строку


def is_valid_date(date_str):
    """
    Проверяет, является ли строка валидной датой в формате 'YYYY-MM-DD'.

    :param date_str: Строка даты.
    :return: True, если дата валидна, иначе False.
    """
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def get_days_difference(date_str1, date_str2):
    """
    Возвращает разницу в днях между двумя датами.

    :param date_str1: Первая дата в формате 'YYYY-MM-DD'.
    :param date_str2: Вторая дата в формате 'YYYY-MM-DD'.
    :return: Разница в днях.
    """
    try:
        date1 = datetime.strptime(date_str1, "%Y-%m-%d")
        date2 = datetime.strptime(date_str2, "%Y-%m-%d")
        return (date2 - date1).days
    except ValueError:
        return None  # Если хотя бы одна из дат некорректна, возвращаем None


def convert_to_qdate(date_str):
    """
    Преобразует строку даты в объект QDate для использования в PyQt.

    :param date_str: Дата в формате 'YYYY-MM-DD'.
    :return: Объект QDate.
    """
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return QDate(date_obj.year, date_obj.month, date_obj.day)
    except ValueError:
        return QDate.currentDate()  # Если ошибка в преобразовании, возвращаем текущую дату
