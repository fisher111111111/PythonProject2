# from sqlalchemy import Column, Integer, String, create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
#
# # Базовый класс для деклараций
# Base = declarative_base()
#
# # Определение модели пользователя
# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     username = Column(String)
#     email = Column(String)
#
# # Настройка подключения к базе данных
# db_path = r"C:\\Users\\user\\PycharmProjects\\GraphQL_API_DB\\users.db"
# connection_string = f'sqlite:///{db_path}'
# engine = create_engine(f'sqlite:///{db_path}', echo=True)
# Base.metadata.create_all(engine)
#
# # Создание фабрики сессий
# Session = sessionmaker(bind=engine)
# session = Session()
#
# # Новый пользователь
# new_user = User(name='Paul', email='paul@example.com')
#
# # Добавляем пользователя в базу данных
# session.add(new_user)
# session.commit()
#
# # Завершаем работу с сессией
# session.close()

from sqlalchemy import inspect
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


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
