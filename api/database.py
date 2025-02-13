from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient("mongodb://localhost:27017/")

# створили взяли бд
db = client["my_database"]

# взяли створили колекцію
collection = db["recipes"]
# collection.insert_one({"name": "John", "ingradients": ["ss","aa"],"instructions": "ssssss"})

