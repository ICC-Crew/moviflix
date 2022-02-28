from fastapi import APIRouter

router = APIRouter(
     prefix="/movies",
    tags=["movies"],
)

@router.get("")
async def getmovies(): 
    return {"message": "Welcome to the movies page!"}
