from fastapi import FastAPI
from database import collection
from models import Recipe
from typing import List
from routes import router
from fastapi.staticfiles import StaticFiles
import logging
import subprocess
app = FastAPI()

# app.mount("/media", StaticFiles(directory=UPLOAD_DIR), name="media")
app.include_router(router)


# @app.get('/recipes/', response_model=List[Recipe])
# async def read_root():
#     recipes = await collection.find().to_list(100) 
#     return(recipes)
    # return({"hello": "hello"})

# @app.post('/recipes/')
# async def reed_root():
#     return({"hello": "hello"})

# @app.get('recipes/{item_id}')
# async def reed_root(item_id:int):
#     return({"hello": "hello"})

# @app.get('recipes/')
# async def reed_root():
#     return({"hello": "hello"})