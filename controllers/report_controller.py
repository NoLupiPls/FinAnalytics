from PyQt5.QtWidgets import QMessageBox
from views.report_view import ReportView
from models.database import Database
from models.transaction import Transaction
from datetime import datetime, timedelta


class ReportController:
    def __init__(self, main_window):
        # Инициализация базы данных и главного окна
        self.database = Database()
        self.main_window = main_window

    def generate_report(self, period):
        """
        Генерирует отчет по транзакциям за определенный период.

        :param period: Строка, представляющая период (например, "Последний месяц", "За год").
        :return: Список транзакций за выбранный период.
        """
        # Фильтрация транзакций по выбранному периоду
        transactions = self.database.get_transactions()
        filtered_transactions = self.filter_transactions_by_period(transactions, period)

        # Отображаем отчет в соответствующем окне
        report_dialog = ReportView(filtered_transactions)
        report_dialog.exec_()

    def filter_transactions_by_period(self, transactions, period):
        """
        Фильтрует транзакции по выбранному периоду.

        :param transactions: Список всех транзакций.
        :param period: Период для фильтрации.
        :return: Список отфильтрованных транзакций.
        """
        # Определение даты окончания для фильтрации
        end_date = datetime.today()
        start_date = None

        if period == "Последний месяц":
            start_date = end_date - timedelta(days=30)
        elif period == "Последние 3 месяца":
            start_date = end_date - timedelta(days=90)
        elif period == "Последние 6 месяцев":
            start_date = end_date - timedelta(days=180)
        elif period == "За год":
            start_date = end_date - timedelta(days=365)

        if not start_date:
            return transactions

        # Фильтрация транзакций по дате
        filtered_transactions = [
            transaction for transaction in transactions
            if datetime.strptime(transaction.date, "%Y-%m-%d") >= start_date
        ]

        return filtered_transactions

    def show_report(self, period):
        """
        Открывает окно с отчетом по транзакциям за выбранный период.

        :param period: Строка с периодом отчета.
        """
        try:
            self.generate_report(period)
        except Exception as e:
            QMessageBox.critical(self.main_window, "Ошибка", f"Не удалось сгенерировать отчет: {str(e)}")
