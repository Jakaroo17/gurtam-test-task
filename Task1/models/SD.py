from sqlalchemy import Column, Integer,String,Float
from models.database import Base

# Импорт необходимых библиотек для работы с БД


# Описания дата класса и конструктора по умолчанию. 
class SD(Base):
    # Название таблицы в которую будут вставляться данные
    __tablename__ = 'sd'

    # Описание полей, первичного ключа и типы данных в бд
    id = Column(Integer,primary_key = True)
    date = Column(String)
    time = Column(String)
    lat1 = Column(Float)
    lat2 = Column(String)
    lon1 = Column(Float)
    lon2 = Column(String)
    speed = Column(Integer)
    course = Column(Float)
    height = Column(Float)
    sats = Column(Integer)

    # Конструктор по умолчанию, который принимает массив и создает объект данных
    def __init__(self,parameters: list):
        self.date = parameters[0]
        self.time = parameters[1]
        self.lat1 = parameters[2]
        self.lat2 = parameters[3]
        self.lon1 = parameters[4]
        self.lon2 = parameters[5]
        self.speed = parameters[6]
        self.course = parameters[7]
        self.height = parameters[8]
        self.sats = parameters[9]
        