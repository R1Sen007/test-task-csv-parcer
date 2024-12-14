# *Проект csv-parcer*

## Авторы
 - [Павел Тыртин](https://github.com/R1Sen007)

## Технологии
### backend
 - FastAPI (0.115.6)
 - Sqlalchemy (2.0.36)
 - pandas (2.2.3)
 - aiosqlite (0.20.0)
### server
 - uvicorn


## Описание:

*Пользователи сервиса могут отправлять csv-файлы с полями `saddr` и `dur`, для вычисления `avgDur` и сохранения в бд.*


## Как развернуть проект:

- Клонировать репозиторий
```
git clone https://github.com/R1Sen007/test-task-csv-parcer.git
```
- Создать .env файл в соответствии с .env.example
- Cоздать виртуальное окружение и активировать его в терминале:
```
cd test-task-csv-parcer
python -m venv venv
source venv/bin/activate
```
- Установить зависимости:
```
pip install -r requirements.txt
```
- Провести миграции:
```
alembic upgrade head
```
- Запуск:
```
uvicorn app.main:app --reload
```

- Для теста перейти по `http://localhost:8000/docs`
