from database import collection, collection_vocabulary
from models import Recipe, RecipeCreate, RecipeUpdate
from models import Vocabulary, VocabularyCreate
from bson import ObjectId
import os
from datetime import datetime
from fastapi import APIRouter,File,UploadFile ,HTTPException
from fastapi.responses import FileResponse
import aiofiles
import random


async def get_recipes(page, limit):
    if page and limit:
        start_number = (page - 1) * limit
        end_number = page * limit
        total_count_in_bd = await collection.count_documents({})
        if end_number > total_count_in_bd:
            end_number = total_count_in_bd 
            start_number = (total_count_in_bd//limit) * limit
            if end_number == start_number:
                start_number = start_number - limit
        total_count_document = end_number - start_number
        documents = await collection.find().sort("title",1).skip(start_number).limit(total_count_document).to_list(None)
        return [serialize_recipe(document) for document in documents]
        
    else:
        recipes = await collection.find().to_list(100) 
        return [serialize_recipe(recipe) for recipe in recipes]


# async def create_recipe(recipe_data: RecipeCreate) -> str:
#     recipe_dict = recipe_data.model_dump()
#     new_recipe = await collection.insert_one(recipe_dict)
#     return str(new_recipe.inserted_id)


async def get_recipe_by_id(id:str):
    recipe = await collection.find_one({"_id": ObjectId(id)})
    return serialize_recipe(recipe)


async def update_recipe_by_id(id:str, recipe_update_data: RecipeUpdate):
    # recipe_update_data = recipe_update_data
    update_fiels = {key:value for key,value in recipe_update_data.model_dump().items() if value is not None}
    await collection.update_one({"_id": ObjectId(id)},{"$set":update_fiels})
    update_recipe = await collection.find_one({"_id": ObjectId(id)})

    return serialize_recipe(update_recipe)

async def delete_recipe_by_id(recipe_id:str):
    recipe = await collection.find_one({"_id": ObjectId(recipe_id)})
    if recipe is None:
        return {"error" : "not found"}
    rezult = await collection.delete_one({"_id": ObjectId(recipe_id)})
    if rezult.deleted_count == 1:
        return {"message": "Recipe deleted successfully"} 
    else:
        return {"error" : "not deleted"}


def serialize_recipe(recipe: Recipe):
    recipe["_id"] = str(recipe["_id"])
    return recipe


def generate_unique_filename(filename: str) -> str:
    """Генерує унікальне ім'я на основі часу"""
    ext = os.path.splitext(filename)[1]
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f")
    return f"{timestamp}{ext}"

async def upload_img(UPLOAD_DIR,file: UploadFile = File(...)):
    file_data_time_name = generate_unique_filename(file.filename)
    file_location = os.path.join(UPLOAD_DIR, file_data_time_name)
    
    # Асинхронне збереження файлу
    async with aiofiles.open(file_location, "wb") as out_file:
        while chunk := await file.read(1024):  # Читаємо файл частинами по 1024 байти
            await out_file.write(chunk)
    
    return {"filename": file_data_time_name, "saved_path": file_location}



async def create_recipe(recipe_data: RecipeCreate) -> str:
    recipe_dict = recipe_data.model_dump()
    recipe_dict["is_active"] = True
    new_recipe = await collection.insert_one(recipe_dict)
    return str(new_recipe.inserted_id)


async def get_count_documents():
    return {"count" : await collection.count_documents({})}

# //////////////// english ////////////////////
async def get_count_vocabulary():
    return {"count" : await collection_vocabulary.count_documents({})}


async def create_vocabulary(vocabulary_data: VocabularyCreate) -> str:
    vocabulary_dict = vocabulary_data.model_dump()
    new_vocabulary = await collection_vocabulary.insert_one(vocabulary_dict)
    return str(new_vocabulary.inserted_id)

async def serialize_vocabulary(vocabulary: Vocabulary):
    vocabulary["_id"] = str(vocabulary["_id"])
    return vocabulary


async def get_random_pair_in_vocabulary():
    count = await collection_vocabulary.count_documents({})
    if count == 0:
        return None  # Якщо колекція порожня, повертаємо None
    
    random_index = random.randint(0, count - 1)  # Випадковий індекс
    random_doc = await collection_vocabulary.find().skip(random_index).limit(1).to_list(length=1)
    
    return await serialize_vocabulary(random_doc[0]) if random_doc else None

async def get_vocabulary_by_id(id:str):
    vocabulary = await collection_vocabulary.find_one({"_id": ObjectId(id)})
    return await serialize_vocabulary(vocabulary)
