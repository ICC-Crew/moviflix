from fastapi import APIRouter, Depends
from ..database.connection import get_database
from ..crud.movies import get_movies,get_movie_by_id
from ..models.movie import Movie
from typing import List

router = APIRouter(
     prefix="/movies",
    tags=["movies"],
)

@router.get("",response_description="List all movies in DB",response_model=List[Movie])
async def getmovies(db = Depends(get_database)): 
    movieList = await get_movies(db)
    return movieList


@router.get("/{movieId}",response_description="Find a single movie with its MongoDB ID",response_model=Movie)
async def getmovie(movieId : str, db = Depends(get_database)): 
    movie = await get_movie_by_id(db,movieId)
    return movie
