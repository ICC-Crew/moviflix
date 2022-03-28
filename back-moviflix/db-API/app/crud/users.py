from fastapi import Query
from ..database.connection import AsyncIOMotorClient
from bson import ObjectId
from ..models.user import UserIns
from typing import List

database_name = "moviflixDB"
collection_name= "users"

async def fetch_users(conn: AsyncIOMotorClient):
    row = await conn[database_name][collection_name].find().to_list(length=1000)
    return row

async def fetch_user_by_id(conn: AsyncIOMotorClient,userId:str):
    row = await conn[database_name][collection_name].find_one({"_id": ObjectId(userId)}) 
    return row    

async def fetch_user_by_user_name(conn: AsyncIOMotorClient,userName:str):
    row = await conn[database_name][collection_name].find_one({"userName": userName}) 
    return row 

async def add_user(conn : AsyncIOMotorClient, user:UserIns):
    userDict = UserIns(**user.dict())
    newMovie = await conn[database_name][collection_name].insert_one(userDict.dict())
    return newMovie.inserted_id
