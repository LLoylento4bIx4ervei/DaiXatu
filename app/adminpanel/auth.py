from sqladmin import Admin
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from starlette.responses import RedirectResponse
from app.exceptions import IncorrectUserMailPas

from app.user.auth import authenticate_user, create_access_token
from app.user.dependencies import get_current_user


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        email, password = form["username"], form["password"]

        user = await authenticate_user(email, password)
        if not user:
            raise IncorrectUserMailPas
        access_token = create_access_token({"sub":str(user.id)})
        request.session.update({"token": access_token})

        return True

    async def logout(self, request: Request) -> bool:
        # Usually you'd want to just clear the session
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")

        
            


        if not token:
            return False
        
        

        # Check the token in depth
        return True


authentication_backend = AdminAuth(secret_key="...")

