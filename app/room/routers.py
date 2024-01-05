from fastapi import APIRouter
from app.room.osnovaroom import BaseRoom
import asyncio
from fastapi_cache.decorator import cache

router = APIRouter()

@router.get('/roomsall')
@cache(expire=40)
async def get_allrooms():
    await asyncio.sleep(3)
    return await BaseRoom.get_all()
