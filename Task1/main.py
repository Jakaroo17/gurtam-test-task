# Главная точка входа в приложение


import os
from models.database import DATABASE_NAME
import create_database as db_creator
# Импорт библиотеки для работы с системой, названия базы данных и функции создания базы данных

if __name__ == '__main__':
    # Проверка на наличие базы данных application.sqlite в директории. Если отсутсвует, то создает новую 
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()

