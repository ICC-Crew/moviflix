from fastapi import APIRouter, Depends
from ..database.connection import get_database
from ..crud.movies import get_movies
from ..models.movie import Movie
from typing import List

router = APIRouter(
     prefix="/movies",
    tags=["movies"],
)

@router.get("",tags=["movies"],response_description="List all movies in DB",response_model=List[Movie])
async def getmovies(db = Depends(get_database)): 
    movieList = await get_movies(db)
    return movieList
