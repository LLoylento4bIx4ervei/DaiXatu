from sqlalchemy import  Column, Integer, ForeignKey,Date
from app.database import Base

class Purchases(Base):
    __tablename__ = "purchases"

    id = Column(Integer, primary_key=True)
    room_id = Column(ForeignKey("rooms.id"))
    user_id = Column(ForeignKey("users.id"))
    bought = Column(Date, nullable=False)
    