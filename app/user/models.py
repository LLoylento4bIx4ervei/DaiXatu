from app.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Users(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String)
    last_name = Column(String)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    rooms_id = Column(ForeignKey("rooms.id"))