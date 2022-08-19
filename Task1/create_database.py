from sqlite3 import InterfaceError
from models.database import create_db,Session
from models.M import M
from models.SD import SD
from parser import package_splitter

# Метод создания базы данных с вызовом метода наполнения таблиц значениями
def create_database(load_fake_data: bool = True):
    create_db()
    if _load_fake_data:
        _load_fake_data(Session())
    

# Метод с вставкой отпарсинговых значений в бд
def _load_fake_data(session: Session):
    # Конечно входные данные можно подавать откуда-то извне, но решил оставить значения в теле метода, так как решение тестового задания итак overengineered с моей стороны
    # Но решил добавить больше тестовых данных для проверки
    packages = "#SD#04012011;135515;5544.6025;N;03739.6834;E;35;215;110;7\r\n#M#груз доставлен\r\n#M#груз потерян\r\n#SD#10042022;101015;5214.5125;S;13739.6234;W;100;351;112;12"
    for package in str.split(packages,'\r\n'): # Прохождение циклом по элементам списка после деления \r\n. Список состоит из 4 элементов
        data_object = return_package_object(package_splitter(package)) #Вызов Switch-case после парсинга пакета данных 
        session.add(data_object) # добавление данных в таблицу БД текущей сессии

        #Проверка на исключительные ситуации. Если вдруг, в таблицу бд, попытаться вставить значения несоотвествующего класса, то программа завершит выполнение с ошибкой InterfaceError,
        # Так мы явно укажем что произошла исключительная ситуация без остановки выполнения программы. Однако проверку на соотвествие данным можно сделать в классе SD и M 
    try: 
        session.commit()
        session.close()
        print("DB Data push succeded")
        # Если все успешно, то данные внесутся в таблицу окончательно и будет разорвано соединение
    except InterfaceError:
        print("Data Push failed") 


# Аналог switch-case, так как в python такая конструкция отсутсвует. Принимает результат парсинга пакетов и создает объект в зависимости от первого элемента списка.
# Плюс данного подхода в том, что таблиц может быть больше чем две и данный switch-case можно безболезненно расширять, добавляя дата классы соотвествующим таблицам  
def return_package_object(package:list):
    return {
       package[0] == 'SD': SD(package[1]),
       package[0] == 'M': M(package[1])
    }[True]



