from passlib.context import CryptContext
from pydantic import EmailStr
from app.user.osnovauser import BaseUser
from datetime import datetime, timedelta
from jose import jwt
from app.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_hash_password(password:str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)



def create_access_token(data:dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=60)
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(
        to_encode,settings.SECRET_KEY, settings.ALGORITHM
    )
    return encoded_jwt



async def authenticate_user(email: EmailStr, password:str):
    user = await BaseUser.get_one(email = email)
    if not (user and verify_password(password, user.password)):
        return None
    return  user
