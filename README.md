# Финансовый трекер

Финансовый трекер — это приложение для управления личными финансами. Оно позволяет пользователям добавлять, редактировать и удалять транзакции, анализировать расходы и доходы за выбранный период, а также генерировать отчеты.

## Функциональность

- **Добавление и редактирование транзакций**: Учет доходов и расходов с указанием суммы, категории и даты.
- **Категории транзакций**: Управление категориями, такими как "Продукты", "Транспорт", "Развлечения", "Зарплата" и т.д.
- **Фильтрация транзакций**: Возможность отображать данные за последние месяцы, полгода, год и за все время.
- **Отчеты и графики**: Генерация графиков расходов и доходов за выбранный период для наглядного анализа.

## Технологии

- **Python 3.9+**
- **PyQt5** — библиотека для создания графического интерфейса.
- **SQLite** — встроенная база данных для хранения транзакций.
- **Matplotlib** — библиотека для построения графиков.

## Структура проекта
```
FinAnalytics/
├── main.py                   # Запуск приложения
├── config.py                 # Конфигурации и настройки
├──dist/
│   └── FinTracker.exe        # Программма
├── models/                   # Логика данных и модели
│   ├── database.py           # Работа с базой данных (SQLite)
│   └── transaction.py        # Модель транзакции
├── views/                    # Интерфейс пользователя (UI)
│   ├── main_window.py        # Главный экран
│   ├── add_transaction.py    # Окно добавления транзакции
│   └── report_view.py        # Экран для отчетов и графиков
├── controllers/              # Логика взаимодействия между UI и моделями
│   ├── main_controller.py    # Основной контроллер
│   └── report_controller.py  # Контроллер для отчетов
├── resources/                # Ресурсы приложения (иконки, стили)
│   ├── icons/                # Иконки
│   └── styles.qss            # Стили (Qt Style Sheets)
└── utils/                    # Утилиты
    └── helpers.py            # Вспомогательные функции
```

## Установка

1. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/NoLupiPls/FinAnalytics.git
   ```
2. Перейдите в директорию проекта:
   ```bash
   cd FinAnalytics
   ```
3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

## Запуск

Для запуска приложения выполните следующую команду:

```bash
python main.py
```

## Использование

1. **Добавление транзакций**: Нажмите на кнопку "Добавить транзакцию", введите необходимые данные и сохраните.
2. **Редактирование транзакций**: Выберите транзакцию в списке и нажмите "Редактировать".
3. **Фильтрация**: В разделе отчета выберите интересующий период (последний месяц, 3 месяца, 6 месяцев и т.д.).
4. **Просмотр отчетов**: Сгенерируйте отчеты по доходам и расходам для анализа.

## Поддержка

Если у вас есть вопросы или предложения по улучшению проекта, вы можете создать issue или pull request в этом репозитории.

## Лицензия

Проект распространяется под лицензией MIT. Подробности можно найти в файле `LICENSE`.

---

Этот README описывает ключевые аспекты проекта и предоставляет инструкции по установке, использованию и структуре проекта.
