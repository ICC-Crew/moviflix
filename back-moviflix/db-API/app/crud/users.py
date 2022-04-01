from collections import UserDict
from fastapi import Query
from ..database.connection import AsyncIOMotorClient
from ..models.user import UserIns, UserLogin, UpdateStructureUser
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

    if usernameCheckerUnique is not None:
        if emailCheckerUnique is not None:
            newUser = await conn[database_name][collection_name].insert_one(userDict.dict())
            return_structure.userAdded = str(newUser.inserted_id);
        else:
            return_structure.error = f"L'email choisi '{userDict.email}' existe déjà, veuillez en choisir un différent"
    else:
        return_structure.error = f"Le pseudo choisi  '{userDict.userName}' existe déjà, veuillez en choisir un différent"
        
    return return_structure

async def fetch_login_user_name_and_pwd(conn: AsyncIOMotorClient, user:UserLogin):
    userDict = UserLogin(**user.dict())
    row = await conn[database_name][collection_name].find_one(userDict.dict())
    return row 

async def fetch_user_watched_movies(conn: AsyncIOMotorClient, userId:PyObjectId):
    ratingList = await conn[database_name]["userOpinions"].find({"userId": userId}).to_list(length=1000)
    movieIdList = [el["movieId"] for el in ratingList]

    movieList = await conn[database_name]["movies"].find({"_id": {"$in": movieIdList}}, projection={"_id": True, "title": True, "movieCoverUrl": True}).to_list(length=1000)

    if movieList is not None and movieList != []:
        for movL in movieList:
            for movRating in ratingList:
                if movRating["movieId"] == movL["_id"]:
                    movL["rating"] = movRating["rating"]
                    ratingList.remove(movRating)

    return movieList