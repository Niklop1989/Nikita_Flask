import httpx

from fastapi import APIRouter
from sqlalchemy.util import await_only

router = APIRouter(prefix='/comments')

# BASE_URL = 'https://jsonplaceholder.org/comments'
BASE_URL = 'https://jsonplaceholder.typicode.com/comments'


@router.get('/')
async def get_posts():
    # return {'comments':'hi'}
    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_URL)
        return response.json()
