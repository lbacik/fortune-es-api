import logging
from fastapi import FastAPI
from api import api
from elasticsearch_client import create as create_es_connection


logging.basicConfig(level=logging.INFO)


def init_app():

    create_es_connection()

    app = FastAPI(
        title = 'Fortune search api',
        version = '0.1.0',
    )

    app.include_router(api, prefix='/api/v1')

    return app


app = init_app()

