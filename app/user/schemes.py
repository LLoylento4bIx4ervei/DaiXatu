from pydantic import BaseModel, EmailStr


class UserOut(BaseModel):
    password:str
    email:EmailStr

    class Config:
        orm_mode = True