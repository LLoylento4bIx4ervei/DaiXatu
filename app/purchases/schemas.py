from pydantic import BaseModel
from datetime import date

class PurchasesOut(BaseModel):
    room_id:int
    user_id:int
    bought:date
    
    class Config:
        orm_mode = True