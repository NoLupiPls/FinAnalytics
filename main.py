import sys
import os

from PyQt5.QtWidgets import QApplication

from views.main_window import MainWindow
from controllers.main_controller import MainController
from config import Config


DIR_DEFAULT = os.path.join(os.path.expanduser("~"), ".FinAnalytics")


def main():
    # Создаем экземпляр приложения
    app = QApplication(sys.argv)

    # Применяем стили, если указаны в конфигурации
    if Config.USE_STYLESHEET:
        with open(Config.STYLESHEET_PATH, "r") as style_file:
            app.setStyleSheet(style_file.read())

    # Создаем главное окно
    main_window = MainWindow()

    # Инициализируем контроллер с главным окном
    controller = MainController()

    # Запускаем главный цикл приложения
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
