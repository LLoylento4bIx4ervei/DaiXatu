from fastapi import APIRouter, Depends,Request
from fastapi.templating import Jinja2Templates

from app.purchases.routers import pur_all

router = APIRouter()

templates = Jinja2Templates("app/templates")


@router.get("/myroom")
async def get_my_room(
    request: Request,
    rooms = Depends(pur_all)
):
    return templates.TemplateResponse(name="xatu.html", context={"request":request, "rooms":rooms})
