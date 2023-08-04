# Приложение для учета трат пользователей

## Старт проекта

Создать `.env` файл и заполнить его необходимыми значениями:

SECRET_KEY=...
DB_NAME=...
DB_USER=...
DB_PASSWORD=...
DB_HOST=...
DB_PORT=...

## Настройте отправку писем на электронную почту

Я использую -> "smtp.yandex.com"
EMAIL_HOST_USER = ...
EMAIL_HOST_PASSWORD = ... -> в `.env` файле

## Установить модули:

`install psycopg2`
`install Pillow`
`install django-environ`
`install environ`

Установить зависимости:
`poetry install`

Активировать виртуальное окружения:
`poetry shell`

Создать миграции:
`poetry run python manage.py makemigrations`

Накатить миграции:
`poetry run python manage.py migrate`

Создать суперпользователя для доступа к админке:
`poetry run python manage.py createsuperuser`

Запуск приложения:
`poetry run python manage.py runserver`

## Панель администратора

url ->  `http://localhost:8000/admin/`
