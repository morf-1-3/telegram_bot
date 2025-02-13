from fastapi import APIRouter,File,UploadFile ,HTTPException
from fastapi.responses import FileResponse
import aiofiles
import logging
from services import *
from models import Recipe
import os
from fastapi import Query


UPLOAD_DIR = "media"  # Каталог для збереження файлів
os.makedirs(UPLOAD_DIR, exist_ok=True)

router = APIRouter()

@router.get('/recipes/')
async def show_recipes(
                    page: int = Query(None, ge=1),
                    limit: int = Query(None, ge=1, le=100)
                ):
    return await get_recipes(page=page,limit=limit)


# @router.post('/recipes/')
# async def add_recipe(recipe_data: RecipeCreate):
#     new_recipe_id = await create_recipe(recipe_data)
#     return {"recipe_id" : new_recipe_id}


@router.get('/recipes/{recipe_id}')
async def show_recipes_by_id(recipe_id:str):
    return await get_recipe_by_id(recipe_id)

@router.patch('/recipes/{recipe_id}')
async def change_recipes_by_id(recipe_id:str,recipe_update_data: RecipeUpdate):
    return await update_recipe_by_id(recipe_id,recipe_update_data)

@router.delete('/recipes/{recipe_id}')
async def delete_recipe(recipe_id:str):
    return await delete_recipe_by_id(recipe_id)




@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    return await upload_img(UPLOAD_DIR,file)


@router.get("/media/{filename}")
async def get_image(filename: str):
    file_path = os.path.join(UPLOAD_DIR, filename)

    if not os.path.exists(file_path):
        return {"error": "File not found"}

    return FileResponse(file_path)



@router.post('/recipes/')
async def add_recipe(recipe_data: RecipeCreate):
    new_recipe_id = await create_recipe(recipe_data)
    return {"recipe_id" : new_recipe_id}


@router.get('/get_count/')
async def get_count():
    return await get_count_documents()
