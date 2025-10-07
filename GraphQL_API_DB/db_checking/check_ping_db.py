from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError

# Путь к базе данных SQLite
db_path = r"C:\\Users\\user\\PycharmProjects\\GraphQL_API_DB\\users.db"

# Формируем строку подключения
connection_string = f'sqlite:///{db_path}'

# Создаем движок базы данных
engine = create_engine(connection_string)

try:
    # Попытка открытия соединения
    with engine.connect() as conn:
        # Тестируем работоспособность, выполняя простейший запрос
        result = conn.execute(text("SELECT name FROM sqlite_master WHERE type='table';")).fetchall()
        print("Подключение прошло успешно. Таблицы в базе данных:")
        for table in result:
            print(table[0])
except OperationalError as err:
    print(f"Ошибка подключения: {err}")
