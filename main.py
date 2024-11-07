import argparse
import logging
import sys
import os

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

from views.main_window import MainWindow
from controllers.main_controller import MainController
from config import Config


DIR_DEFAULT = os.path.join(os.path.expanduser("~"), ".FinAnalytics")

LOGGING_FORMATTER = "[%(asctime)s] [%(levelname)s] [%(funcName)s] %(message)s"


def parse_args() -> argparse.Namespace:
    """Parses cli arguments

    Returns:
          argparse.Namespace: parsed arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        "--app-dir",
        type=str,
        required=False,
        help=f"path to application directory (with finance_tracker.db) (Default: {DIR_DEFAULT})",
        default=DIR_DEFAULT,
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="specify to enable DEBUG logging into console",
        default=False,
    )
    parser.add_argument("-v", "--version", action="version", version=Config.__version__)
    return parser.parse_args()


def main():
    args = parse_args()
    # Initialize logging with DEBUG level in case of --debug or WARNING otherwise
    logging.basicConfig(level=logging.DEBUG if args.debug else logging.WARNING, format=LOGGING_FORMATTER)

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

    # Показываем главное окно
    # main_window.show()

    # Запускаем главный цикл приложения
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
