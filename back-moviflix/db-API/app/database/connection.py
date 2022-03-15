from motor.motor_asyncio import AsyncIOMotorClient
    
class DataBase:
    client : AsyncIOMotorClient = None

db=DataBase()

async def get_database():
    return db.client

async def connect_to_mongo():
    db.client = AsyncIOMotorClient('mongodb://moviflix_db_1:27017') # A mettre dans une variable d'environnement
    
async def close_mongo_connection():
    db.client.close()
