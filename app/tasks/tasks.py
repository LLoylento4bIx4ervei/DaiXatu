from app.tasks.celery import celery
from PIL import Image
from pathlib import Path




@celery.task
def obr_pic(
    path:str,
):
    img_path = Path(path)
    img = Image.open(img_path)
    img_resized_big = img.resize((1000,200))
    img_resized_small = img.resize((100,20))
    img_resized_big.save(f"app/static/images/resized_big{img_path.name}")
    img_resized_small.save(f"app/static/images/resized_small{img_path.name}")


