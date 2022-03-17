from ..database.connection import AsyncIOMotorClient
from bson import ObjectId

database_name = "moviflixDB"

async def get_movies(conn: AsyncIOMotorClient):
    row = await conn[database_name]["movies"].find().to_list(length=1000)
    return row

async def get_movie_by_id(conn: AsyncIOMotorClient,movieId:str):
    row = await conn[database_name]["movies"].find_one({"_id": ObjectId(movieId)}) 
    return row    