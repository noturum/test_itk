Django приложение для загрузки и хранения данных в базе данных PostgreSQL. Для запуска сервера нужно собрать образ docker с помощью команды:

docker-compose build
и запусть контейнеры с помощью команды:

docker-compose up

Файл переменных среды .env.copy заменить на .env:

Для API определены следующие роуты:

upload/: [POST] загрузка xlsx файла
json/ [GET]: вывод модели в json
doc/: [GET] документация swagger
