from fastapi import UploadFile, APIRouter
import shutil
from app.tasks.tasks import obr_pic




router = APIRouter()


@router.post("/imagerooms")
async def  hotel_image(name:int,file:UploadFile):
    image_path = f"app/static/images/{name}.webp"
    with open(image_path,"wb+") as file_obj:
        shutil.copyfileobj(file.file, file_obj)
    obr_pic.delay(image_path)

