from fastapi import APIRouter, Response
from app.exceptions import IncorrectUserMailPas, UserAlreadyExistsException
from app.user.osnovauser import BaseUser
from app.user.schemes import UserOut
from app.user.auth import get_hash_password, authenticate_user, create_access_token

router = APIRouter()



@router.get("/userall")
async def all_user():
    return await BaseUser.get_all()


@router.post('/userregister')
async def reg_user(user_data: UserOut):
    user_in = await BaseUser.get_all(email=user_data.email)
    if user_in:
        raise UserAlreadyExistsException
    user_hash_password = get_hash_password(user_data.password)
    await BaseUser.add(email= user_data.email, password=user_hash_password)


@router.post('/userlogin')
async def get_login(responce:Response, user_data:UserOut):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise IncorrectUserMailPas
    access_token = create_access_token({"sub":str(user.id)})
    responce.set_cookie("daixatu_access_token", access_token, httponly=True)
    return access_token


@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie("daixatu_access_token")
    



    
