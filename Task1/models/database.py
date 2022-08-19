from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 
# Импортирование необходимых библиотек для работ с БД


# Название БД
DATABASE_NAME = "application.sqlite"
# Строка для соединения с базой данных sqlite
engine = create_engine(f'sqlite:///Task1/{DATABASE_NAME}')
# Создания экзепляра сессии для выполнения операций на БД 
Session = sessionmaker(bind=engine)

# Объявление таблиц в декларативном стиле. Данный объект наследуют все дата классы
Base = declarative_base()


def create_db():
    Base.metadata.create_all(engine)


