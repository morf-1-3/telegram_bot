from motor.motor_asyncio import AsyncIOMotorClient

# client = AsyncIOMotorClient("mongodb://localhost:27017/")
# client = AsyncIOMotorClient("mongodb://mongo:rhwkDKoIuBhvIPiQPopbzTRBuxzmtIwM@mainline.proxy.rlwy.net:45623")
client = AsyncIOMotorClient("mongodb://mongo:XxMXchiutmxzJAUBQCEGHkrOsjlEtwjp@metro.proxy.rlwy.net:31526")


# створили взяли бд
db = client["my_database"]

# взяли створили колекцію
collection = db["recipes"]
# collection.insert_one({"name": "John", "ingradients": ["ss","aa"],"instructions": "ssssss"})

collection_vocabulary = db["vocabulary"]
