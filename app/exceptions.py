from typing import Any, Dict, Optional
from typing_extensions import Annotated, Doc
from fastapi import HTTPException, status


class UserExceptions(HTTPException):
    status_code = 400
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExistsException(UserExceptions):
    status_code = status.HTTP_409_CONFLICT
    detail = "Пользователь уже существует"


class IncorrectUserMailPas(UserExceptions):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Неверная почта или пароль"




class DependenciesException(HTTPException):
    status_code = 400
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class TokenExpiredException(DependenciesException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Истек токен"


class NotTokenException(DependenciesException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Нет токена"


class IncorrectFormatToken(DependenciesException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Неверный формат токена"