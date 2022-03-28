from fastapi import Query
from ..database.connection import AsyncIOMotorClient
from bson import ObjectId
from ..models.movie import MovieIns,UpdatedMovie
from typing import List

database_name = "moviflixDB"
collection_name= "movies"

async def fetch_movies(conn: AsyncIOMotorClient):
    row = await conn[database_name][collection_name].find().to_list(length=1000)
    return row

async def fetch_movie_by_id(conn: AsyncIOMotorClient,movieId:str):
    row = await conn[database_name][collection_name].find_one({"_id": ObjectId(movieId)}) 
    return row    

async def add_movie(conn : AsyncIOMotorClient, movie:MovieIns):
    movieDict = MovieIns(**movie.dict())
    newMovie = await conn[database_name][collection_name].insert_one(movieDict.dict())
    return newMovie.inserted_id

async def add_movies(conn : AsyncIOMotorClient, movies : List[MovieIns]):
    newMovies = await conn[database_name][collection_name].insert_many(movies) 
    return newMovies.inserted_id

async def update_movie(conn : AsyncIOMotorClient,movie:UpdatedMovie,movieId:str):
    movieDict = UpdatedMovie(**movie.dict())
    updatedMovie = await conn[database_name][collection_name].update_one({"_id": ObjectId(movieId)}, {"$set": movieDict.dict()})
    return updatedMovie.modified_count