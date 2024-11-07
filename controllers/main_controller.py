from PyQt5.QtWidgets import QApplication, QMessageBox, QDialog
from views.main_window import MainWindow
from views.add_transaction import AddTransactionDialog
from views.report_view import ReportView
from models.database import Database
from models.transaction import Transaction


class MainController:
    def __init__(self):
        # Инициализация базы данных и главного окна
        self.database = Database()
        self.main_window = MainWindow()

        # Подключение сигналов к обработчикам
        self.main_window.add_button.clicked.connect(self.add_transaction)
        self.main_window.edit_button.clicked.connect(self.edit_transaction)
        self.main_window.delete_button.clicked.connect(self.delete_transaction)
        self.main_window.report_button.clicked.connect(self.show_report)

        # Загрузка данных транзакций
        self.load_transactions()

        # Показ главного окна
        self.main_window.show()

    def load_transactions(self):
        """
        Загружает транзакции из базы данных и отображает их в основном окне.
        """
        transactions = self.database.get_transactions()
        self.main_window.set_transactions(transactions)

    def add_transaction(self):
        """
        Открывает диалог для добавления новой транзакции.
        """
        dialog = AddTransactionDialog()
        if dialog.exec_() == QDialog.Accepted:
            transaction_data = dialog.get_transaction_data()
            transaction = Transaction(
                date=transaction_data['date'],
                amount=transaction_data['amount'],
                category=transaction_data['category'],
                type=transaction_data['type'],
                description=transaction_data['description']
            )
            self.database.add_transaction(transaction)
            self.main_window.add_transaction_to_table(transaction)

    def edit_transaction(self):
        """
        Открывает диалог для редактирования выбранной транзакции.
        """
        transaction_id = self.main_window.get_selected_transaction_id()
        if not transaction_id:
            QMessageBox.warning(self.main_window, "Ошибка", "Выберите транзакцию для редактирования")
            return

        transaction = self.database.get_transaction_by_id(transaction_id)
        dialog = AddTransactionDialog()
        dialog.date_input.setDate(transaction.date)
        dialog.amount_input.setText(str(transaction.amount))
        dialog.category_input.setCurrentText(transaction.category)
        dialog.type_input.setCurrentText(transaction.type)
        dialog.description_input.setText(transaction.description or "")

        if dialog.exec_() == QDialog.Accepted:
            updated_data = dialog.get_transaction_data()
            transaction.date = updated_data['date']
            transaction.amount = updated_data['amount']
            transaction.category = updated_data['category']
            transaction.type = updated_data['type']
            transaction.description = updated_data['description']
            self.database.update_transaction(transaction)
            self.load_transactions()

    def delete_transaction(self):
        """
        Удаляет выбранную транзакцию.
        """
        transaction_id = self.main_window.get_selected_transaction_id()
        if not transaction_id:
            QMessageBox.warning(self.main_window, "Ошибка", "Выберите транзакцию для удаления")
            return

        reply = QMessageBox.question(
            self.main_window, "Подтверждение",
            "Вы уверены, что хотите удалить выбранную транзакцию?",
            QMessageBox.Yes | QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            self.database.delete_transaction(transaction_id)
            self.load_transactions()

    def show_report(self):
        """
        Открывает окно отчета.
        """
        transactions = self.database.get_transactions()
        dialog = ReportView(transactions)
        dialog.exec_()


def main():
    import sys
    app = QApplication(sys.argv)
    controller = MainController()
    sys.exit(app.exec_())
