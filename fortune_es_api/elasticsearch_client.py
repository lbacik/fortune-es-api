import os
import logging
from elasticsearch import Elasticsearch, logger
from dotenv import load_dotenv


load_dotenv()

es: Elasticsearch = None


def create() -> None:
    global es

    ES_HOST: str = os.getenv('ES_HOST')

    logging.info(f'Connecting to Elasticsearch: {ES_HOST}')

    es = Elasticsearch(
        ES_HOST,
        http_auth=(os.getenv('ES_USER'), os.getenv('ES_PASS')), 
        scheme=os.getenv('ES_SCHEME'),
        port=os.getenv('ES_PORT'),
    )

    logger.setLevel(logging.ERROR)


def es_search(query: str) -> dict:
    global es
    return es.search(
        index=os.getenv('INDEX_NAME'), 
        q=query,
        size=200,
        default_operator='AND',
    )
