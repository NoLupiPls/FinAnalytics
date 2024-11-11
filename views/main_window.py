from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QLabel, QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView
)
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Настройка главного окна
        self.setWindowTitle("Финансовый трекер")
        self.setGeometry(100, 100, 800, 400)
        self.setWindowIcon(QIcon('./resources/icons/icon.png'))

        # Создание главного виджета
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Основной вертикальный layout
        self.main_layout = QVBoxLayout(self.central_widget)

        # Заголовок
        self.title_label = QLabel("Финансовый трекер", self)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.title_label)

        # Таблица транзакций
        self.transaction_table = QTableWidget()
        self.transaction_table.setColumnCount(5)
        self.transaction_table.setHorizontalHeaderLabels(["Дата", "Сумма", "Категория", "Тип", "Описание"])
        self.transaction_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.transaction_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.transaction_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.main_layout.addWidget(self.transaction_table)

        # Панель управления с кнопками
        self.button_layout = QHBoxLayout()

        # Кнопка добавления транзакции
        self.add_button = QPushButton("Добавить транзакцию")
        self.button_layout.addWidget(self.add_button)

        # Кнопка редактирования транзакции
        self.edit_button = QPushButton("Редактировать транзакцию")
        self.button_layout.addWidget(self.edit_button)

        # Кнопка удаления транзакции
        self.delete_button = QPushButton("Удалить транзакцию")
        self.button_layout.addWidget(self.delete_button)

        # Кнопка для отображения отчетов
        self.report_button = QPushButton("Отчеты")
        self.button_layout.addWidget(self.report_button)

        self.main_layout.addLayout(self.button_layout)

        # Сообщение о пустом списке (по умолчанию скрыто)
        self.no_data_label = QLabel("Нет доступных транзакций", self)
        self.no_data_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.no_data_label)
        self.no_data_label.setVisible(False)


    def set_transactions(self, transactions):
        """
        Обновляет таблицу транзакций.

        :param transactions: Список транзакций для отображения.
        """
        self.transaction_table.setRowCount(len(transactions))

        for row, transaction in enumerate(transactions):
            self.transaction_table.setItem(row, 0, QTableWidgetItem(transaction.date))
            print("ggg: ", transaction.amount)
            self.transaction_table.setItem(row, 1, QTableWidgetItem(f"{transaction.amount:.2f}"))
            self.transaction_table.setItem(row, 2, QTableWidgetItem(transaction.category))
            self.transaction_table.setItem(row, 3, QTableWidgetItem(transaction.type_))
            self.transaction_table.setItem(row, 4, QTableWidgetItem(transaction.description or ""))

        # Показываем или скрываем сообщение о пустом списке
        self.no_data_label.setVisible(len(transactions) == 0)


    def get_selected_transaction_id(self):
        """
        Возвращает ID выбранной транзакции.

        :return: ID транзакции или None, если транзакция не выбрана.
        """
        selected_row = int(self.transaction_table.currentRow()) + 1
        print(f"Selected row: {selected_row}")
        return selected_row


    def add_transaction_to_table(self, transaction):
        """
        Добавляет новую транзакцию в таблицу.

        :param transaction: Объект транзакции для добавления.
        """
        row = self.transaction_table.rowCount()
        self.transaction_table.insertRow(row)
        self.transaction_table.setItem(row, 0, QTableWidgetItem(transaction.date))
        self.transaction_table.setItem(row, 1, QTableWidgetItem(f"{transaction.amount:.2f}"))
        self.transaction_table.setItem(row, 2, QTableWidgetItem(transaction.category))
        self.transaction_table.setItem(row, 3, QTableWidgetItem(transaction.type_))
        self.transaction_table.setItem(row, 4, QTableWidgetItem(transaction.description or ""))


    def update_transaction_in_table(self, row, transaction):
        """
        Обновляет существующую транзакцию в таблице.

        :param row: Номер строки для обновления.
        :param transaction: Объект транзакции для обновления.
        """
        self.transaction_table.setItem(row, 0, QTableWidgetItem(transaction.date))
        self.transaction_table.setItem(row, 1, QTableWidgetItem(f"{transaction.amount:.2f}"))
        self.transaction_table.setItem(row, 2, QTableWidgetItem(transaction.category))
        self.transaction_table.setItem(row, 3, QTableWidgetItem(transaction.type_))
        self.transaction_table.setItem(row, 4, QTableWidgetItem(transaction.description or ""))


    def delete_selected_transaction(self):
        """
        Удаляет выбранную транзакцию из таблицы.
        """
        selected_row = self.transaction_table.currentRow()
        if selected_row >= 0:
            self.transaction_table.removeRow(selected_row)
