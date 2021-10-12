# Сервис справочник
***

## Возможности сервиса
***
* Импорт данных csv
* Создание данных
* Чтение данных
* Обновление данных
* Удаления данных
* работа в разных СУБД

## Требование сервиса
***
* `python 3.10`
* библиотеки
  * `FastApi`
  * `sqlalchemy`
  * `databases`
  * `uvicorn`
  * драйвер зависимости от типа СУБД
  
## Запуск сервиса
***
1. оределение системных переменых в environments
   * `DATABASE_URL = sqlite:///./test.db;` - url database 
   * `LOGGER_CONFIG = logger.json;` -setting logger
   * `FILE_CSV = data.csv;` - import csv data

2. Запустите файл `migrations.py` этот скрипт отвечает на создание базы данных сервиса
3. Запустите сервис `asgi.py`


