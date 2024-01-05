# DaiXatu
Этот репозиторий о небольшой части backend разработки интерфейса "покупки" квартиры.
# Запуск приложения
Для запуска необходима команда:

`uvicorn app.main:app --reload` (необходимо находиться в корневой директории проекта).
# Celery
Для запуска Celery используется команда:

`celery --app=app.tasks.celery:celery worker -l INFO -P solo`
# Dockerfile
Команда для запуска Dockerfile:

`docker build .`
# Docker compose
Для запуска сервисов БД, Celery, Redis необходимо использовать файл docker-compose.yml и команды:

`docker compose build`
`docker compose up`
