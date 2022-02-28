from fastapi import APIRouter, Depends
from ..database import connection

router = APIRouter(
     prefix="/movies",
    tags=["movies"],
)

@router.get("")
async def getmovies(db = Depends(connection.get_db)): 
    movies = db.movies
    movieList = await movies.find().to_list(length=100)
    return {"message": movieList[0]["actors"]}
