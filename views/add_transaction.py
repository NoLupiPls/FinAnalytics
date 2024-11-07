from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QComboBox, QPushButton, QDateEdit
)
from PyQt5.QtCore import QDate
from config import Config


class AddTransactionDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Настройка диалогового окна
        self.setWindowTitle("Добавить транзакцию")
        self.setFixedSize(400, 390)

        # Основной layout
        self.layout = QVBoxLayout(self)

        # Поле для ввода даты
        self.date_label = QLabel("Дата:")
        self.date_input = QDateEdit()
        self.date_input.setDate(QDate.currentDate())
        self.date_input.setCalendarPopup(True)

        # Поле для ввода суммы
        self.amount_label = QLabel("Сумма:")
        self.amount_input = QLineEdit()
        self.amount_input.setPlaceholderText("Введите сумму")

        # Поле для выбора категории
        self.category_label = QLabel("Категория:")
        self.category_input = QComboBox()
        self.category_input.addItems(Config.TRANSACTION_CATEGORIES)

        # Поле для выбора типа транзакции (доход или расход)
        self.type_label = QLabel("Тип:")
        self.type_input = QComboBox()
        self.type_input.addItems(["Доходы", "Расходы"])

        # Поле для ввода описания
        self.description_label = QLabel("Описание:")
        self.description_input = QLineEdit()
        self.description_input.setPlaceholderText("Необязательно")

        # Кнопки "Сохранить" и "Отмена"
        self.button_layout = QHBoxLayout()
        self.save_button = QPushButton("Сохранить")
        self.cancel_button = QPushButton("Отмена")
        self.button_layout.addWidget(self.save_button)
        self.button_layout.addWidget(self.cancel_button)

        # Добавляем все виджеты на layout
        self.layout.addWidget(self.date_label)
        self.layout.addWidget(self.date_input)
        self.layout.addWidget(self.amount_label)
        self.layout.addWidget(self.amount_input)
        self.layout.addWidget(self.category_label)
        self.layout.addWidget(self.category_input)
        self.layout.addWidget(self.type_label)
        self.layout.addWidget(self.type_input)
        self.layout.addWidget(self.description_label)
        self.layout.addWidget(self.description_input)
        self.layout.addLayout(self.button_layout)

        # Подключаем сигналы к кнопкам
        self.save_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)


    def get_transaction_data(self):
        """
        Возвращает данные транзакции, введенные пользователем.

        :return: Словарь с полями транзакции.
        """
        return {
            "date": self.date_input.date().toString("yyyy-MM-dd"),
            "amount": float(self.amount_input.text()) if self.amount_input.text() else 0.0,
            "category": self.category_input.currentText(),
            "type_": self.type_input.currentText(),
            "description": self.description_input.text()
        }


    def accept(self):
        """
        Переопределение метода accept() для проверки введенных данных перед закрытием окна.
        """
        # Проверка, что сумма введена корректно
        try:
            amount = float(self.amount_input.text())
            if amount <= 0:
                raise ValueError("Сумма должна быть больше нуля.")
        except ValueError as e:
            self.amount_input.setStyleSheet("border: 1px solid red;")
            self.amount_input.setPlaceholderText("Введите корректную сумму")
            return

        super().accept()
