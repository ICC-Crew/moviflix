from turtle import update
from fastapi import Query
from ..database.connection import AsyncIOMotorClient
from ..models.user_opinion import UserOpinionIns, UpdateStructureUserOpinion, UserOpinionStruct
from bson import ObjectId, errors
from typing import List
from ..models.common import PyObjectId
from .movies import fetch_movie_by_id
from .users import fetch_user_by_id

database_name = "moviflixDB"
collection_name= "userOpinions"

async def fetch_user_opinions(conn: AsyncIOMotorClient):
    row = await conn[database_name][collection_name].find().to_list(length=1000)
    return row

async def fetch_user_opinion_by_id(conn: AsyncIOMotorClient,userId:PyObjectId):
    row = await conn[database_name][collection_name].find_one({"_id": userId}) 
    return row

async def fetch_user_opinions_by_user_id(conn: AsyncIOMotorClient, userId:PyObjectId):
    row = await conn[database_name][collection_name].find({"userId": userId}).to_list(length=1000)
    return row

async def fetch_user_opinion_with_movie_id(conn: AsyncIOMotorClient, userId:PyObjectId, movieId:PyObjectId):
    row = await conn[database_name][collection_name].find_one({"userId": userId, "movieId": movieId})
    return row

async def add_user_opinion(conn : AsyncIOMotorClient, userOpinion:UserOpinionStruct):
    return_structure = UpdateStructureUserOpinion()

    userOpinionDict = UserOpinionIns(**userOpinion.dict())
    
    userExistChecker = await fetch_user_by_id(conn, userOpinionDict.userId)

    # Check if user exists in DB
    if userExistChecker is None:
        return_structure.error = f"User ID {userOpinionDict.userId} does not exist"
        return return_structure

    movieExistChecker = await fetch_movie_by_id(conn, userOpinionDict.movieId)

    # Check if movie exists in DB
    if movieExistChecker is None:
        return_structure.error = f"Movie ID {userOpinionDict.movieId} does not exist"
        return return_structure
    
    
    # Check if user opinion exists in DB
    userOpinionCheckerUnique = await conn[database_name][collection_name].find_one({"userId": userOpinionDict.userId, "movieId": userOpinionDict.movieId})

    if userOpinionCheckerUnique is None:
        newUserOpinion = await conn[database_name][collection_name].insert_one(userOpinionDict.dict()) 
        return_structure.userOpinionAdded = newUserOpinion.inserted_id
    else:
        updatedUserOpinion = await conn[database_name][collection_name].update_one({"_id": userOpinionCheckerUnique["_id"]}, {"$set": {"rating": userOpinionDict.rating}})
        return_structure.userOpinionAdded = f"Modified : {updatedUserOpinion.modified_count}"
        
    return return_structure
