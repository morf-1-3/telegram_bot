from pydantic import BaseModel
from bson import ObjectId
from typing import List, Optional
from datetime import datetime



class Recipe(BaseModel):
    name: str
    ingradients: List[str]
    instructions : str

    class Config:
        json_encoders = {
            ObjectId: str
        }


# class RecipeCreate(BaseModel):
#     title: str
#     ingredients: List[str]
#     instructions: str

class RecipeUpdate(BaseModel):
    title: Optional[str] = None
    ingredients: Optional[List[str]] = None
    instructions: Optional[str] = None

class RecipeCreate(BaseModel):
    title: str
    description: str
    ingredients: List[str]
    categories: List[str]
    cooking_time: str
    difficulty: str
    steps: List[str]
    image_id_in_telegram: Optional[str] = None
    user_id: int
    # author_id: str
    # create_at: datetime
    # likes: int
    # image_name: str
    # is_active: bool




    

