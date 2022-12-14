# gurtam-test-task
 
Тестовое задание для компании gurtam. Было решено выполнять его на python, так как знания TCL отсутсвует, а времени учить его не было. В некоторой степени решение задания overengineered, так как было решено использовать базу данных для первого задания и несколько способов решения для второго.

Текст задания:

'1'. Разработайте программу, которая будет парсировать строки такого формата:
#TP#DATA\r\n
где
'#' – символ разделитель
TP – тип пакета
DATA – поле данных пакета
\r\n – признак конца пакета (символы перевода строки и возврата каретки)
Содержимое поля DATA зависит от типа пакета. Программа должна корректно 
обрабатывать любые входящие строки данного формата, корректно разбирать их на 
составляющие, подготавливать их к записи в базу данных (приводить к соответствующим 
типам данных) и просто выводить составляющие на экран.
Описание доступных типов пакетов:
1. Пакет “SD”. Поле DATA содержит следующие поля:
#SD#date;time;lat1;lat2;lon1;lon2;speed;course;height;sats\r\n
Пример пакета: 
#SD#04012011;135515;5544.6025;N;03739.6834;E;35;215;110;7
Описание полей:
date - дата в формате DDMMYYYY, в UTC
time - время в формате HHMMSS, в UTC
lat1;lat2 - широта (5544.6025;N) – приводить к одному дробному числу
lon1;lon2 - долгота (03739.6834;E) – приводить к одному дробному числу
Примечание: Формат широты и долготы такой же, как и в RMC строке протокола 
NMEA (http://ru.wikipedia.org/wiki/NMEA#RMC-.D1.81.D1.82.D1.80.D0.BE.D0.BA.D0.B0)
speed - скорость, целое число, км/ч
course - курс, целое число, градусы
height - высота, целое число, в метрах
sats - количество спутников, целое число
2. Пакет “M”. Поле DATA содержит одно текстовое поле с сообщением.
Пример пакета: #M#груз доставлен

'2'. Разработайте программу, которая из исходного значения 0x5FABFF01 выведет на 
экран значения дополнительных параметров. Первый дополнительный параметр 
содержится во втором байте исходного значения, второй дополнительный параметр 
является инверсным значением 7-го бита исходного значения. Третий дополнительный 
параметр является зеркальным отображением 17-20 го бита(20 бит исходного значения 
является 1 битом третьего дополнительного параметра, 17 бит исходного значения 
является 4 битом третьего дополнительного параметра).



Собственно про решение:

1 Задание. 

Необходимо для начала установить ORM SQLAlchemy для того чтобы возможно было работать с базой данных SQLITE, для этого в терминале необходимо выполнить следующие действия

1. Установка необходимых модулей (глобально)

```
pip3 install -r requirements.txt
```
1.1 Либо же на виртуальное окружение (для того чтобы не загружать модули глобально в систему.
```
pip install virtualenv
python3 -m venv env
source env/bin/activate
(env) pip3 install -r requirements.txt
```
2. Запуск скрипта
```
python3 Task1/main.py
```

В Task1 находятся следующие файлы


+ Task1
    + models
        + __init__.py      - Файл для инциализации ORM SQLAlchemy
        + database.py      - Python-скрипт с инциализацией БД и созданием сессий
        + M.py             - Дата класс для пакетов M, а также определение полей
        + SD.py            - Дата-класс для пакетов SD, а также определение полей
+ application.sqlite    - База данных в которых хранится вся информация
+ create_database.py    - Python-скрипт с методами вставки информации информации из бд, использующая функции parser.py
+ main.py               - Главная точка входа в приложение
+ parser.py             - Python-скрипт с методами парсинга строк

В каждом файле есть комментарии, которые могут чуть лучше объяснить код, если возникнут трудности с пониманием.


2.Задание 

Данное задание было решено двумя способами
+ Легкий для реализации, но неэффективный по памяти и времени выполнения
+ Чуть сложнее для реализации, но эффективнее по памяти и времени выполнения

Для запуска скрипта необходимо прописать
```
python3 Task2/main.py
```
Какие-то дополнительные модули устанавливать не надо. В коде есть все нужные комментарии
