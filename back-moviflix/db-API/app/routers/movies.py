from fastapi import APIRouter, Depends
from ..database.connection import get_database
from ..crud.movies import get_movies

router = APIRouter(
     prefix="/movies",
    tags=["movies"],
)

@router.get("",tags=["movies"])
async def getmovies(db = Depends(get_database)): 
    movieList = await get_movies(db)
    return {"message": movieList[0]["actors"]}
