
### Автоматизированные тесты для проверки API документации сайта [Full Stack FastAPI Project](https://dashboard.fast-api.senior-pomidorov.ru/)

### Описание проекта
Это проект для проверки API документации сайта [Full Stack FastAPI Project](https://dashboard.fast-api.senior-pomidorov.ru/), который 
содержит набор автоматизированных тестов для [Full Stack FastAPI Project - Swagger UI](https://api.fast-api.senior-pomidorov.ru/docs#/), написанных
на Python с использованием фреймворка `pytest` и создания отчетности в Allure Report. 
Тесты проверяют функциональность различных эндпойнтов API, включая получение токена авторизации, получение списка items, получение информации об items по ID, создание, обновление и удаление item. 

Проект составлен с использованием Python и его библиотек, и предназначен для обеспечения непрерывного тестирования [Full Stack FastAPI Project - Swagger UI](https://api.fast-api.senior-pomidorov.ru/docs#/) и автоматического
обнаружения ошибок. Позволяет быстро и эффективно проверять работоспособность API после внесения 
изменений в код или в данные.

С самой API документацией сайта [Full Stack FastAPI Project](https://dashboard.fast-api.senior-pomidorov.ru/) можно ознакомиться по ссылке 
https://api.fast-api.senior-pomidorov.ru/docs#/

### Структура проекта

```markdown

├── src/
│   ├── api/
│   │   ├── api_items.py
│   │   └── login_access.py
│   ├── enums_item/
│   │   ├── const_url.py
│   │   └── invalid_data.py
│   ├── item_models/
│   │   ├── data_error_model.py
│   │   └── data_model_items.py
│   ├── scenarios/
│   │   ├── scenario_items_invalid.py
│   │   └── scenario_items_valid.py
│   └── utils/
│       ├── urls_item.py
│       ├── validator_all_items.py      
│       ├── validator_error_items.py
│       └── validator_item_data.py 
├── tests/
│   ├── test_invalid_item.py
│   ├── test_login_items.py
│   ├── test_valid_item.py
│   └── test_wrong_login.py
├── .gitignore
├── .python-version
├── conftest.py
├── main.py
├── pyproject.toml
├── README.md
└── ux.lock
```

### Расположение проекта
Проект расположен на удаленном репозитории на [**Github**](https://github.com/fisher111111111/PythonProject2)

### Установка фреймворка для запуска автоматизированных тестов 

Это проект, создан с помощью инструмента **uv** — современного менеджера и шаблонизатора для Python-проектов.

### Как скачать и развернуть проект локально

#### Шаг 1. Клонирование репозитория
```bash
git clone https://github.com/fisher111111111/PythonProject2.git
cd PythonProject2
```
#### Шаг 2. Установка uv (если не установлен)
```bash
pip install uv
```
#### Шаг 3. Создание и активация виртуального окружения (рекомендуется)
Создание окружения
```bash
python -m venv .venv
```
Активация окружения
#### for Windows
```bash
.venv\Scripts\activate
```
#### for Linux/macOS
```bash
source .venv/bin/activate
```
!!! По окончании работы для деактивации и выхода из виртуального 
окружения используйте команду
```bash
deactivate
``` 

#### Шаг 4. Установка зависимостей
Для установки зависимостей указанных в pyproject.toml, используйте:
```bash 
uv pip install -r pyproject.toml 
```
или установите необходимые пакеты вручную в список значения поля dependencies = []

```
[project]
...
dependencies = [
    "allure>=2.35.1",
    "dotenv>=1.1.1",
    "faker>=37.3.0",
    "pytest>=8.3.5",
    "requests>=2.32.3",
]
 ...
```

#### Шаг 5. Проверка работоспособности
Для проверки работоспособности проекта запустите основной скрипт:
```bash
uv run main.py
```
Подтверждением успешной установки проекта и окружения uv 
будет полученный ответ:
```
Hello from PythonProject2!
```
##### Примечание
   Для получения актуальной информации по uv используйте:
```bash
uv --help
```
#### Шаг 6. Поверка кода (необязательный)
   В случае внесения изменений в код проекта, либо в иных 
необходимых случаях есть возможность использовать интегрированные 
в проект линтеры:
- blake  (форматировать код проекта)
- isort  (отсортировать импорты в файлах проекта)
- flake8 (проверить стиль и ошибки в файлах проекта)

   Для запуска линтеров отправьте в терминале соответствующие команды
```bash
black .        
isort .        
flake8 .        
```

### Запуск автоматизированных тестов на Python
Для запуска тестов используйте в терминале команду:
```bash
pytest
```
Для запуска тестов с сохранением результатов в Allure используйте команду:
```bash
python -m pytest tests -v -s --alluredir=allure-results
```

Для получения отчета в Allure Report используйте команду:
```bash
allure serve allure-results
```
Для обновления отчетов в Allure Report перед запуском
команды <span style="color: green;">python -m pytest tests -v -s --alluredir=allure-results</span> 
очистите папку allure-results/ командой:
#### for Windows :
```bash
Remove-Item allure-results* -Recurse -Force
```  
#### for Linux/macOS
```bash
rm -rf allure-results/*
```
 


### Авторы
**Рыбальченко Алексей**
### Контакты
Telegram: [@Rybalchenko_Alexei]()