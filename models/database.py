import sqlite3
from config import Config
from models.transaction import Transaction


class Database:
    def __init__(self):
        """Инициализация базы данных и подключение к SQLite."""
        self.connection = sqlite3.connect(Config.DATABASE_PATH)
        self.cursor = self.connection.cursor()
        self.create_tables()


    def create_tables(self):
        """Создает таблицы в базе данных, если они не существуют."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                type_ TEXT NOT NULL,
                description TEXT
            )
        """)
        self.connection.commit()


    def add_transaction(self, transaction):
        """
        Вставка транзакции в базу данных.

        :param transaction: объект класса Transaction
        """
        query = """
        INSERT INTO transactions (date, amount, category, type_, description)
        VALUES (?, ?, ?, ?, ?)
        """
        # Извлекаем данные из объекта transaction
        self.cursor.execute(query, (
            transaction.date,
            transaction.amount,
            transaction.category,
            transaction.type_,
            transaction.description
        ))
        self.connection.commit()


    def get_transactions(self):
        """
        Возвращает все транзакции из базы данных.

        :return: Список объектов Transaction.
        """
        query = "SELECT * FROM transactions"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()

        transactions = []
        for row in rows:
            transaction = Transaction(
                transaction_id=row[0],
                date=row[1],
                amount=row[2],
                category=row[3],
                type_=row[4],
                description=row[5]
            )
            transactions.append(transaction)

        return transactions


    def get_transaction_by_id(self, transaction_id):
        """
        Получает транзакцию по ID из базы данных.

        :param transaction_id: ID транзакции
        :return: Словарь с данными транзакции или None, если транзакция не найдена
        """
        query = "SELECT date, amount, category, type_, description FROM transactions WHERE id = ?"
        self.cursor.execute(query, (transaction_id,))
        result = self.cursor.fetchone()\

        print("Результат запроса:", result)  # Отладочный вывод

        if result:
            # Преобразуем результат в словарь для удобного использования
            return {
                "date": result[0],
                "amount": result[1],
                "category": result[2],
                "type_": result[3],
                "description": result[4]
            }
        return None  # Возвращаем None, если транзакция не найдена


    def get_all_transactions(self):
        """Возвращает все транзакции из базы данных."""
        self.cursor.execute("SELECT * FROM transactions ORDER BY date DESC")
        return self.cursor.fetchall()


    def get_transactions_by_category(self, category):
        """Возвращает транзакции по указанной категории."""
        self.cursor.execute("""
            SELECT * FROM transactions WHERE category = ? ORDER BY date DESC
        """, (category,))
        return self.cursor.fetchall()


    def get_transactions_by_date_range(self, start_date, end_date):
        """Возвращает транзакции в указанном диапазоне дат."""
        self.cursor.execute("""
            SELECT * FROM transactions WHERE date BETWEEN ? AND ? ORDER BY date DESC
        """, (start_date, end_date))
        return self.cursor.fetchall()


    def delete_transaction(self, transaction_id):
        """Удаляет транзакцию по ID."""
        self.cursor.execute("DELETE FROM transactions WHERE id = ?", (transaction_id,))
        self.connection.commit()


    def update_transaction(self, transaction_id, date, amount, category, type_, description=None):
        """Обновляет данные о транзакции по ID."""
        self.cursor.execute("""
            UPDATE transactions
            SET date = ?, amount = ?, category = ?, type = ?, description = ?
            WHERE id = ?
        """, (date, amount, category, type_, description, transaction_id))
        self.connection.commit()


    def get_total_by_type(self, type_):
        """Возвращает общую сумму транзакций для указанного типа ('Income' или 'Expense')."""
        self.cursor.execute("""
            SELECT SUM(amount) FROM transactions WHERE type = ?
        """, (type_,))
        result = self.cursor.fetchone()
        return result[0] if result[0] is not None else 0


    def close(self):
        """Закрывает соединение с базой данных."""
        self.connection.close()
