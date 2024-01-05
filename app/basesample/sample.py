from sqlalchemy import select, insert, delete
from app.database import ASYNC_SESSION_MAKER


class Osnova:
    model = None

    @classmethod
    async def get_one(cls, **filter_by):
        async with ASYNC_SESSION_MAKER() as session:
             query = select(cls.model.__table__.columns).filter_by(**filter_by)
             answer = await session.execute(query)
             return answer.mappings().one_or_none()


    @classmethod
    async def get_all(cls, **filter_by): 
         async with ASYNC_SESSION_MAKER() as session:
             query = select(cls.model.__table__.columns).filter_by(**filter_by)
             answer = await session.execute(query)
             return answer.mappings().all()


    @classmethod
    async def add(cls, **data):
        async with ASYNC_SESSION_MAKER() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()


    @classmethod
    async def find_by_id(cls, model_id: int):
        async with ASYNC_SESSION_MAKER() as session:
            query = select(cls.model.__table__.columns).filter_by(id=model_id)
            answer = await session.execute(query)
            return answer.mappings().one_or_none()
        

    @classmethod
    async def del_it(cls, model_id: int):
        async with ASYNC_SESSION_MAKER() as session:
            query = delete(cls.model).filter_by(id=model_id)
            await session.execute(query)
            await session.commit()


    