
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

### Запуск автоматизированных тестов на Python 

Для установки фреймворка необходимо установить соответствующие библиотеки:

```bash
pip install -r requirements.txt
````

Для запуска тестов используйте команду:
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

### Авторы
**Рыбальченко Алексей**
### Контакты
e-mail: [alexey_1979@mail.ru]()

Telegram: [@Rybalchenko_Alexei]()