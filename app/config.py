from pydantic_settings import BaseSettings
from typing import Literal

class Settings(BaseSettings):
    

    DB_HOST: str
    DB_NAME: str
    DB_PASSWORD: str
    DB_PORT: int
    DB_USER: str


   

    SECRET_KEY:str
    ALGORITHM:str

   

    REDIS_HOST:str
    REDIS_PORT:int

    @property
    def DATABASE_URL(self):
        return (f'postgresql+asyncpg://{self.DB_USER}:'
                f'{self.DB_PASSWORD}@{self.DB_HOST}:'
                f'{self.DB_PORT}/{self.DB_NAME}')
    

   


    class Config:
        env_file = ".env"


settings = Settings()
print(settings.DB_PORT)