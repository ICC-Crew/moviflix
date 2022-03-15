from ..database.connection import AsyncIOMotorClient
from ..models.movie import Movie

database_name = "moviflixDB"

async def get_movies(conn: AsyncIOMotorClient):
    row = await conn[database_name]["movies"].find().to_list(length=1000)
    return row