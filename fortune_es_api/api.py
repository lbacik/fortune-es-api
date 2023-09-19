import logging
from fastapi import APIRouter
from elasticsearch_client import es_search


api = APIRouter(
    prefix="/search",
)


@api.get("/")
async def search(q: str) -> dict:
    try:
        return es_search(q)
    except Exception as e:
        logging.error(e)
        return {"error": "Something went wrong"}

