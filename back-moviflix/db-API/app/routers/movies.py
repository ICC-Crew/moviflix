from fastapi import APIRouter, Depends
from ..database.connection import get_database
from ..crud.movies import fetch_movies,fetch_movie_by_id,add_movie,update_movie
from ..models.movie import Movie,MovieIns,UpdatedMovie
from typing import List
from fastapi import HTTPException, Body, status
from fastapi.responses import JSONResponse
from ..models.common import PyObjectId

router = APIRouter(
     prefix="/movies",
    tags=["movies"],
)

@router.get("",response_description="List all movies in DB",response_model=List[Movie])
async def get_movies(db = Depends(get_database)): 
    movieList = await fetch_movies(db)
    return movieList

@router.get("/{movieId}",response_description="Find a single movie with its MongoDB ID",response_model=Movie)
async def get_movie(movieId : str, db = Depends(get_database)): 
    movie = await fetch_movie_by_id(db,movieId)
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
