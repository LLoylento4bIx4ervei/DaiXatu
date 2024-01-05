from app.purchases.osnovapurchases import BasePurchases
from app.purchases.schemas import PurchasesOut
from typing import List
from fastapi import APIRouter, Depends
from app.user.models import Users
from app.user.dependencies import get_current_user
from app.user.osnovauser import BaseUser
import asyncio
from fastapi_cache.decorator import cache



router = APIRouter()


@router.get('/pur/{id}')
async def get_byid(id: int) -> List[PurchasesOut]:
    return await BasePurchases.find_by_id(id)



@router.get('/purchasesall')
@cache(expire=20)
async def pur_all() -> List[PurchasesOut]:
    await asyncio.sleep(3)
    return await BasePurchases.get_all()



@router.delete('/purss/{id}')
async def dele_pur(id :int):
    return await BasePurchases.del_it(id)


@router.get('/purssuser')
async def get_purchases(user: Users = Depends(get_current_user)):
    return await BaseUser.find_by_id(user.id)


