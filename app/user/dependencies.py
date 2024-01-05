from fastapi import Depends, Request,HTTPException, status
from jose import jwt, JWTError
from app.config import settings
from datetime import datetime, timedelta
from app.exceptions import IncorrectFormatToken, NotTokenException, TokenExpiredException
from app.user.osnovauser import BaseUser



def get_token(request:Request):
    token = request.cookies.get("daixatu_access_token")
    if not token:
        raise NotTokenException
    return token


async def get_current_user(token: str=Depends(get_token)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)

    except JWTError:
        raise IncorrectFormatToken

    expire: str = payload.get("exp")
    if (not expire) or(int(expire)< datetime.utcnow().timestamp()):
        raise TokenExpiredException
    
    user_id: str = payload.get("sub")
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED) 
    
    user = await BaseUser.find_by_id(int(user_id))
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return user



    
    