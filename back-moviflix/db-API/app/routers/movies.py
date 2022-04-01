from fastapi import APIRouter, Depends
from ..database.connection import get_database
from ..crud.movies import fetch_movie_by_id,add_movie,fetch_movies_with_projection,update_movie,count_movies
from ..models.movie import Movie,MovieIns,UpdatedMovie
from ..models.common import PyObjectId

from typing import List
from fastapi import HTTPException, Body, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

router = APIRouter(
    prefix="/movies",
    tags=["movies"],
)

@router.get("",response_description="List all movies in DB, with projection. If you don't provide any projection field, uses title and movieCoverUrl")
async def get_movies_with_projection(limit:int = 20, page:int = 0, parameters:str = None, db = Depends(get_database)):
    movieList = await fetch_movies_with_projection(db, limit, page, parameters)
    
    # Nothing found in the DB
    if movieList is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nothing was found")
    
    # Nothing found for the desired page
    if movieList == []:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Nothing was found for page {page}. Try to get back to the previous page.")

    for mov in movieList:
        mov["_id"] = str(mov["_id"])

    json_compatible_item_data = jsonable_encoder(movieList)
    return JSONResponse(content=json_compatible_item_data)

@router.get("/count",response_description="Count the number of Movies")
async def number_of_movies(db = Depends(get_database)): 
    number = await count_movies(db)
    if number is not None : 
        return {"number" : number}

    raise HTTPException(status_code=400, detail="Error counting the number of movies")
    
@router.get("/{movieId}",response_description="Find a single movie with its MongoDB ID",response_model=Movie)
async def get_movie(movieId : str, db = Depends(get_database)):
    # Check if the movie ID is valid
    try:
        movieIdToFetch = PyObjectId(movieId)
    except:
        raise HTTPException(status_code=status.HTTP_418_IM_A_TEAPOT, detail=f"The provided user ID '{movieId}' is not a valid Mongo ID")

    movie = await fetch_movie_by_id(db,movieIdToFetch)

    if movie is not None : 
        return movie

    raise HTTPException(status_code=404, detail=f"Movie {movieId} not found")



@router.post("",response_description="Insert a single movie into the DB")
async def insert_movie(movie : MovieIns = Body(...), db=Depends(get_database)):
    movieId = await add_movie(db,movie)
    responseJSON = {"insertedId": str(movieId)}
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=responseJSON)
 
@router.patch("/{movieId}",response_description="Update movie DB")
async def update_one(movieId:str, movie:UpdatedMovie = Body(...),db=Depends(get_database)):
    inserted = await update_movie(db,movie,movieId)
    if inserted == 0:
        raise HTTPException(status_code=404, detail=f"Movie {movieId} not found")
    return {"updated":inserted}