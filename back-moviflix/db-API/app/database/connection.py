import motor.motor_asyncio
import asyncio
    
async def get_db():
    client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://moviflix_db_1:27017')
    db = client.moviflixDB
    try:
        yield db
    finally:
        print("CONNECTION TO DB CLOSED")
        client.close()
