from sqlalchemy import inspect
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base


# Базовый класс для деклараций
Base = declarative_base()



# Настройка подключения к базе данных
db_path = r"C:\\Users\\user\\PycharmProjects\\GraphQL_API_DB\\users.db"
connection_string = f'sqlite:///{db_path}'
engine = create_engine(f'sqlite:///{db_path}', echo=True)

ins = inspect(engine)
columns = ins.get_columns('users')
for col in columns:
    print(col['name'], col['type'])
