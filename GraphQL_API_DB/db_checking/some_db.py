from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text

# Параметры соединения
DB_USER = 'postgres'
DB_PASSWORD = 'usfHO8BAY5'
DB_HOST = 'localhost'  # Например, IP адрес сервера
DB_PORT = '5432'                   # Порт PostgreSQL по умолчанию
DB_NAME = 'app'

# Строка подключения
connection_string = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

# Создаем движок
engine = create_engine(connection_string)

# Создаем сессию
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# print("Подключено успешно!")
try:
    # Простой запрос для проверки доступности базы данных
    result = session.execute(text("SELECT 1"))

    # Извлекаем результат
    data = result.scalars().all()
    if len(data) > 0:
        print("Подключение установлено успешно! Результат:", data)
    else:
        print("Нет результата")

except Exception as e:
    print(f"Ошибка подключения: {e}")
finally:
    session.close()
