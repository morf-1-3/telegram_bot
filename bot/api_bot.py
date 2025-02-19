import aiohttp
import logging

# API_URL = "http://localhost:8000"
API_URL = "https://telegrambot-production-2bd0.up.railway.app/"



async def get_recipes_api(session:aiohttp.ClientSession,limit:int, page:int, URL_END="/recipes/"):
    request_url = API_URL + URL_END
    if limit and page:
        request_url += f"?page={page}&limit={limit}"
    async with session.get(request_url) as response:
        if response.status == 200:
            logging.info(f"🔹 ClientSession ID: {id(session)}")
            return await response.json()  # Парсимо JSON
        else:
            return None

async def add_recipes_api(session:aiohttp.ClientSession,data:dict, URL_END="/recipes/"):
    # print(str(data))
    async with session.post(API_URL + URL_END,json=data) as response:
        if response.status == 200:
            logging.info(f"🔹 ClientSession ID: {id(session)}")
            return await response.json()  # Парсимо JSON
        else:
            logging.info("bed request")

            return None
        
async def get_count_recipes_api(session:aiohttp.ClientSession, URL_END="/get_count/"):
    async with session.get(API_URL + URL_END) as response:
        if response.status == 200:
            logging.info(f"🔹 ClientSession ID: {id(session)}")
            return await response.json()  # Парсимо JSON
        else:
            return None
        

async def get_recipe_by_id_api(session:aiohttp.ClientSession,recipe_id, URL_END="/recipes/"):
    request_url = API_URL + URL_END + recipe_id
    async with session.get(request_url) as response:
        if response.status == 200:
            logging.info(f"🔹 ClientSession ID: {id(session)}")
            return await response.json()  # Парсимо JSON
        else:
            return None
        

async def get_random_word_api(session:aiohttp.ClientSession, URL_END="/vocabulary/"):
    request_url = API_URL + URL_END 
    async with session.get(request_url) as response:
        if response.status == 200:
            logging.info(f"🔹 ClientSession ID: {id(session)}")
            return await response.json()  # Парсимо JSON
        else:
            return None
        

async def get_word_by_id_api(session:aiohttp.ClientSession,recipe_id, URL_END="/vocabulary/"):
    request_url = API_URL + URL_END + recipe_id
    async with session.get(request_url) as response:
        if response.status == 200:
            logging.info(f"🔹 ClientSession ID: {id(session)}")
            return await response.json()  # Парсимо JSON
        else:
            return None
