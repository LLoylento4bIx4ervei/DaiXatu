from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis
from sqladmin import Admin, ModelView

from app.adminpanel.auth import authentication_backend
from app.adminpanel.models import PurchasesAdmin, UsersAdmin
from app.config import settings
from app.database import engine
from app.images.router import router as image_router
from app.pages.routers import router as pages_router
from app.purchases.routers import router as purchases_router
from app.room.routers import router as room_router
from app.user.routers import router as user_router

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), "static")


app.include_router(user_router)
app.include_router(room_router)
app.include_router(purchases_router)
app.include_router(pages_router)
app.include_router(image_router)




origins = [
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET","POST","DELETE","PATCH","PUT"],
    allow_headers=["Content-Type","Set-Cookie","Access-Control-Allow-Headers","","Authorizations"]
)






@app.on_event("startup")
def startup():
    redis = aioredis.from_url(f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}")
    FastAPICache.init(RedisBackend(redis),prefix="cache")





admin = Admin(app,engine,authentication_backend=authentication_backend)




admin.add_view(UsersAdmin)
admin.add_view(PurchasesAdmin)
    









