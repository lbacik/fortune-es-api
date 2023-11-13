import logging
from fastapi import APIRouter
from elasticsearch_client import es_search


api = APIRouter(
    prefix="/search",
)


@api.get("/")
async def search(q: str, limit: int = 10, page: int = 0) -> dict:
    try:
        return es_search(q, page, limit)
    except Exception as e:
        logging.error(e)
        return {"error": "Something went wrong"}
