from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Основание для деклараций
Base = declarative_base()

# Определение модели
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

# Соединение с базой данных
db_path = r"C:\\Users\\user\\PycharmProjects\\GraphQL_API_DB\\users.db"
connection_string = f'sqlite:///{db_path}'
engine = create_engine(f'sqlite:///{db_path}', echo=True)
Base.metadata.create_all(engine)

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()

# Новая запись
new_user = User(name='John Doe', email='john.doe@example.com')

# Добавляем запись в базу данных
session.add(new_user)
session.commit()

# Закрываем сессию
session.close()
