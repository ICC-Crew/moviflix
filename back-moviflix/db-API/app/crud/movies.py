from ..database.connection import AsyncIOMotorClient

database_name = "moviflixDB"

async def get_movies(conn: AsyncIOMotorClient):
    row = await conn[database_name]["movies"].find().to_list(length=100)
    return row