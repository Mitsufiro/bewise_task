<div id="badges" align='center'>
    <a>
        <img src="https://img.shields.io/badge/Python-3.10-green?logo=Python">
    </a>
    <a>
        <img src="https://img.shields.io/badge/FastAPI-0.95-green?logo=fastapi&logoColor=black?style=plastic"/>
    </a>
    <a>
        <img src="https://img.shields.io/badge/alembic-1.10-green?logo=alembic&logoColor=black?style=plastic">
    </a>
    <a>
        <img src="https://img.shields.io/badge/postgresql-13-blue?logo=postgresql&logoColor=white">
    </a>
    <a>
        <img src="https://img.shields.io/badge/SQLalchemy-1.4.41-blue?logo=SQLalchemy">
    </a>
    <a>
        <img src="https://img.shields.io/badge/Docker-20.10.16-green?logo=Docker&logoColor=black?style=plastic">
    </a>
</div>

## Клонируем репозиторий:

    git clone https://github.com/Mitsufiro/bewise_task

## Развертывание

`docker-compose up`

## Migrations

При изменении модели данных необходимо создать миграцию

`docker exec app alembic revision --autogenerate -m "New Migration"`

Для применения изменений, необходимо запустить

`docker exec app alembic upgrade head`


## Finally:

• Swagger.

• Подготовлен docker-контейнер с сервисами.

• Загружаются вопросы викторины, неуникальные вопросы отсеиваются и загрузка продолжается пока не достигнет необходимого количества.
    
<img src="screens/post.png" width="400" height="200">

<img src="screens/response.png" width="400" height="200">