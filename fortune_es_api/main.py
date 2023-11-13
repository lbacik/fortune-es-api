import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api import api
from elasticsearch_client import create as create_es_connection


logging.basicConfig(level=logging.INFO)


def init_app():

    create_es_connection()

    app = FastAPI(
        title='Fortune search api',
        version='0.1.0',
    )

    app.include_router(api, prefix='/api/v1')

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app


app = init_app()
