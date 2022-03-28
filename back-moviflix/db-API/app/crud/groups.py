from fastapi import Query
from ..database.connection import AsyncIOMotorClient
from bson import ObjectId
from ..models.group import GroupIns
from typing import List

database_name = "moviflixDB"
collection_name= "groups"

async def fetch_groups(conn: AsyncIOMotorClient):
    row = await conn[database_name][collection_name].find().to_list(length=1000)
    return row

async def fetch_group_by_id(conn: AsyncIOMotorClient,groupId:str):
    row = await conn[database_name][collection_name].find_one({"_id": ObjectId(groupId)}) 
    return row    

async def add_group(conn : AsyncIOMotorClient, group:GroupIns):
    groupDict = GroupIns(**group.dict())
    newMovie = await conn[database_name][collection_name].insert_one(groupDict.dict())
    return newMovie.inserted_id
