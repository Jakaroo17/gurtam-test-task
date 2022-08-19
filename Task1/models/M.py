from sqlalchemy import Column,String,Integer
from models.database import Base
# Импорт необходимых библиотек для работы с БД

# Описания дата класса и конструктора по умолчанию. 
class M(Base):
    # Название таблицы в которую будут вставляться данные
    __tablename__ = 'm'

    # Описание полей, первичных ключей и типы данных в бд
    id = Column(Integer,primary_key = True)
    message = Column(String)

    # Конструктор по умолчанию, который принимает сообщение
    def __init__(self,message: str):
        self.message = message