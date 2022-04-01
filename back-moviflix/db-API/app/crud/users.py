from collections import UserDict
from fastapi import Query
from ..database.connection import AsyncIOMotorClient
from ..models.user import UserIns, UpdateStructureUser, UserLoginSchema
from bson import ObjectId, errors
from typing import List
from ..models.common import PyObjectId

database_name = "moviflixDB"
collection_name= "users"

async def fetch_users(conn: AsyncIOMotorClient):
    row = await conn[database_name][collection_name].find().to_list(length=1000)
    return row

async def fetch_user_by_id(conn: AsyncIOMotorClient,userId:PyObjectId):
    row = await conn[database_name][collection_name].find_one({"_id": userId}) 
    return row    

async def fetch_user_by_user_name(conn: AsyncIOMotorClient,userName:str):
    row = await conn[database_name][collection_name].find_one({"userName": userName}) 
    return row 

async def add_user(conn : AsyncIOMotorClient, user:UserIns):
    return_structure = UpdateStructureUser()

    userDict = UserIns(**user.dict())
    usernameCheckerUnique = await conn[database_name][collection_name].find_one({"userName": userDict.userName})
    emailCheckerUnique = await conn[database_name][collection_name].find_one({"email": userDict.email})

    if usernameCheckerUnique is None:
        if emailCheckerUnique is None:
            newUser = await conn[database_name][collection_name].insert_one(userDict.dict())
            return_structure.userAdded = str(newUser.inserted_id)
        else:
            return_structure.error = f"L'email choisi '{userDict.email}' existe déjà, veuillez en choisir un différent"
    else:
        return_structure.error = f"Le pseudo choisi  '{userDict.userName}' existe déjà, veuillez en choisir un différent"
        
    return return_structure

async def fetch_check_exist_user_login(conn: AsyncIOMotorClient, user:UserLoginSchema):
    userDict = UserLoginSchema(**user.dict())
    row = await conn[database_name][collection_name].find_one(userDict.dict())
    if row is not None:
        return True
    else:
        return False