from sqladmin import ModelView


from app.user.models import Users
from app.purchases.models import Purchases

class UsersAdmin(ModelView,model=Users):
    column_list=[Users.id, Users.email]
    column_details_exclude_list= [Users.password]
    can_delete = False
    name = "Пользователь"
    name_plural = "Пользователи"
    icon = "fa-solid fa-user"


class PurchasesAdmin(ModelView,model=Purchases):
    column_list=[ c.name for c in Purchases.__table__.c]
    
    name = "Покупки"
    name_plural = "Покупки"
    icon = "fa-solid fa-book"