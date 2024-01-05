from app.basesample.sample import Osnova
from app.user.models import Users


class BaseUser(Osnova):
    model = Users