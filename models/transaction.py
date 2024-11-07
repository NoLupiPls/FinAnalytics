class Transaction:
    def __init__(self, date, amount, category, type_, description=None, transaction_id=None):
        """
        Инициализация объекта транзакции.

        :param date: Дата транзакции (в формате строки, например 'YYYY-MM-DD')
        :param amount: Сумма транзакции (положительное число)
        :param category: Категория транзакции (строка)
        :param type_: Тип транзакции ('Доходы' или 'Расходы')
        :param description: Описание транзакции (необязательное поле)
        :param transaction_id: ID транзакции в базе данных (если известно)
        """
        self.transaction_id = transaction_id  # ID в базе данных (None, если это новая транзакция)
        self.date = date
        self.amount = amount
        self.category = category
        self.type_ = type_
        self.description = description


    def to_dict(self):
        """
        Преобразует объект транзакции в словарь для удобной передачи данных.

        :return: Словарь с полями транзакции.
        """
        return {
            "transaction_id": self.transaction_id,
            "date": self.date,
            "amount": self.amount,
            "category": self.category,
            "type": self.type_,
            "description": self.description,
        }


    @staticmethod
    def from_dict(data):
        """
        Создает объект транзакции из словаря данных.

        :param data: Словарь, содержащий данные транзакции.
        :return: Объект Transaction.
        """
        return Transaction(
            transaction_id=data.get("transaction_id"),
            date=data.get("date"),
            amount=data.get("amount"),
            category=data.get("category"),
            type_=data.get("type"),
            description=data.get("description")
        )


    def is_income(self):
        """
        Проверяет, является ли транзакция доходом.

        :return: True, если тип транзакции 'Доходы', иначе False.
        """
        return self.type_ == "Доходы"


    def is_expense(self):
        """
        Проверяет, является ли транзакция расходом.

        :return: True, если тип транзакции 'Расходы', иначе False.
        """
        return self.type_ == "Расходы"


    def __str__(self):
        """
        Возвращает строковое представление объекта транзакции.

        :return: Строка с информацией о транзакции.
        """
        return (f"Transaction(id={self.transaction_id}, date={self.date}, amount={self.amount}, "
                f"category={self.category}, type={self.type_}, description={self.description})")
