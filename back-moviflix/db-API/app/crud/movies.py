from inspect import Parameter
from ..database.connection import AsyncIOMotorClient
from bson import ObjectId
from ..models.movie import MovieIns,UpdatedMovie
from ..models.common import PyObjectId
from typing import List
import ast

database_name = "moviflixDB"
collection_name= "movies"

async def fetch_movies(conn: AsyncIOMotorClient):
    row = await conn[database_name][collection_name].find().to_list(length=1000)
    return row

async def fetch_incomplete_movies(conn : AsyncIOMotorClient):
    row = await conn[database_name][collection_name].find({"fetched":0},{"_id":1,"imdbID":1}).to_list(length=1000)
    return row

async def fetch_movies_with_filtering_by_genre(conn: AsyncIOMotorClient, genres:str, exclude:str):
    print(f"genre {genres} exclude: {exclude}")
    if genres is not None and genres != "":
        params = ""
        for p in genres.split(","):
            params += f"'{p.strip()}',"
        
        filterArray = ast.literal_eval("[" + params + "]")
        
        if exclude is not None and exclude != "":
            moviesToExclude = [] 
            for p in exclude.split(","):
                moviesToExclude.append(PyObjectId(f"{p.strip()}"))
            
            row = await conn[database_name][collection_name].find({"genres": {"$in": filterArray}, "_id": {"$nin": moviesToExclude}},{"_id": 1, "title": 1, "movieCoverUrl": 1}).to_list(length=1000)
        else:        
            row = await conn[database_name][collection_name].find({"genres": {"$in": filterArray}},{"_id": 1, "title": 1, "movieCoverUrl": 1}).to_list(length=1000)
    else:
        row = fetch_movies(conn)

    return row

async def fetch_movie_by_id(conn: AsyncIOMotorClient, movieId:PyObjectId):
    row = await conn[database_name][collection_name].find_one({"_id": movieId}) 
    return row    

async def count_movies(conn:AsyncIOMotorClient):
    number = await conn[database_name][collection_name].count_documents({})
    return number

async def add_movie(conn : AsyncIOMotorClient, movie:MovieIns):
    movieDict = MovieIns(**movie.dict())
    newMovie = await conn[database_name][collection_name].insert_one(movieDict.dict())
    return newMovie.inserted_id

async def add_movies(conn : AsyncIOMotorClient, movies : List[MovieIns]):
    newMovies = await conn[database_name][collection_name].insert_many(movies) 
    return newMovies.inserted_id

async def fetch_movies_with_projection(conn: AsyncIOMotorClient, limit:int, page:int, parameters:str):
    projection = {}

    if parameters is not None and parameters != "":
        params = ""
        for p in parameters.split(","):
            params += f"'{p.strip()}',"

        parametersToProcess = ast.literal_eval("[" + params + "]")

        for param in parametersToProcess:
            projection[param] = True
    
    if projection == {}:
        projection = {"title": True, "movieCoverUrl": True}
    
    row = await conn[database_name][collection_name].find(projection=projection).skip(page * limit).limit(limit).to_list(length=limit) 
    
    return row  

async def update_movie(conn : AsyncIOMotorClient,movie:UpdatedMovie,movieId:str):
    movieDict = UpdatedMovie(**movie.dict())
    updatedMovie = await conn[database_name][collection_name].update_one({"_id": ObjectId(movieId)}, {"$set": movieDict.dict()})
    return updatedMovie.modified_count
