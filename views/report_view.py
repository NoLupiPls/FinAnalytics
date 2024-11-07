from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QLabel, QComboBox, QTableWidget,
    QTableWidgetItem, QHeaderView, QHBoxLayout
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class ReportView(QDialog):
    def __init__(self, transaction_data, parent=None):
        super().__init__(parent)

        # Настройка окна отчета
        self.setWindowTitle("Отчет")
        self.setFixedSize(800, 600)

        # Основной layout
        self.layout = QVBoxLayout(self)

        # Заголовок
        self.title_label = QLabel("Отчет по транзакциям", self)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.title_label)

        # Выбор периода отчета
        self.period_label = QLabel("Выберите период:")
        self.period_input = QComboBox()
        self.period_input.addItems(["Последний месяц", "Последние 3 месяца", "Последние 6 месяцев", "За год"])

        # Обновление отчета при смене периода
        self.period_input.currentIndexChanged.connect(self.update_report)

        # Layout для выбора периода
        self.period_layout = QHBoxLayout()
        self.period_layout.addWidget(self.period_label)
        self.period_layout.addWidget(self.period_input)
        self.layout.addLayout(self.period_layout)

        # Таблица для отображения данных отчета
        self.report_table = QTableWidget()
        self.report_table.setColumnCount(3)
        self.report_table.setHorizontalHeaderLabels(["Категория", "Доход", "Расход"])
        self.report_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.layout.addWidget(self.report_table)

        # Площадка для графика
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        # Данные транзакций
        self.transaction_data = transaction_data

        # Инициализация отчета
        self.update_report()


    def update_report(self):
        """
        Обновляет отчет по выбранному периоду.
        """
        period = self.period_input.currentText()

        # Получение данных по транзакциям за выбранный период
        filtered_data = self.filter_transactions_by_period(period)

        # Обновление таблицы отчета
        self.update_report_table(filtered_data)

        # Обновление графика
        self.update_chart(filtered_data)


    def filter_transactions_by_period(self, period):
        """
        Фильтрует транзакции по выбранному периоду.

        :param period: Период отчета.
        :return: Отфильтрованные данные транзакций.
        """
        # Фильтрация данных по выбранному периоду (примерный код)
        # В реальном приложении здесь будет фильтрация по дате
        return self.transaction_data  # Пока возвращаем все данные без фильтрации


    def update_report_table(self, data):
        """
        Обновляет таблицу с отчетом.

        :param data: Данные транзакций для отображения.
        """
        # Группировка данных по категориям
        report_data = {}
        for transaction in data:
            category = transaction.category
            amount = transaction.amount
            if category not in report_data:
                report_data[category] = {"Доходы": 0, "Расходы": 0}
            if transaction.is_income():
                report_data[category]["Доходы"] += amount
            else:
                report_data[category]["Расходы"] += amount

        # Очистка и заполнение таблицы
        self.report_table.setRowCount(len(report_data))
        for row, (category, values) in enumerate(report_data.items()):
            self.report_table.setItem(row, 0, QTableWidgetItem(category))
            self.report_table.setItem(row, 1, QTableWidgetItem(f"{values['Доходы']:.2f}"))
            self.report_table.setItem(row, 2, QTableWidgetItem(f"{values['Расходы']:.2f}"))


    def update_chart(self, data):
        """
        Обновляет график с данными доходов и расходов по категориям.

        :param data: Данные транзакций для отображения на графике.
        """
        # Очистка текущего графика
        self.figure.clear()

        # Подготовка данных для графика
        categories = []
        income_values = []
        expense_values = []
        report_data = {}

        for transaction in data:
            category = transaction.category
            amount = transaction.amount
            if category not in report_data:
                report_data[category] = {"Доходы": 0, "Расходы": 0}
            if transaction.is_income():
                report_data[category]["Доходы"] += amount
            else:
                report_data[category]["Расходы"] += amount

        for category, values in report_data.items():
            categories.append(category)
            income_values.append(values["Доходы"])
            expense_values.append(values["Расходы"])

        # Построение графика
        ax = self.figure.add_subplot(111)
        ax.bar(categories, income_values, label="Доход", color="green")
        ax.bar(categories, expense_values, label="Расход", color="red", bottom=income_values)
        ax.set_ylabel("Сумма")
        ax.set_title("Доходы и расходы по категориям")
        ax.legend()

        # Обновление отображения графика
        self.canvas.draw()
