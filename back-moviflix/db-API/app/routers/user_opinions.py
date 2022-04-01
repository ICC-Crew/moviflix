from fastapi import APIRouter, Depends
from ..database.connection import get_database
from ..crud.user_opinions import fetch_user_opinions, fetch_user_opinion_by_id, add_user_opinion
from ..models.user_opinion import UserOpinion, UserOpinionIns, UserOpinionStruct
from typing import List
from fastapi import HTTPException, Body, status
from fastapi.responses import JSONResponse
from ..models.common import PyObjectId

router = APIRouter(
     prefix="/useropinions",
    tags=["useropinions"],
)

@router.get("",response_description="List all user opinions in DB",response_model=List[UserOpinion])
async def get_user_opinions(db = Depends(get_database)): 
    userList = await fetch_user_opinions(db)
    return userList

@router.get("/{userOpinionId}",response_description="Find an user opinion with its MongoDB ID",response_model=UserOpinion)
async def get_user_opinion_by_id(userOpinionId : str, db = Depends(get_database)):
    # Check if the user ID is valid
    try:
        userOpinionIdToFetch = PyObjectId(userOpinionId)
    except:
        raise HTTPException(status_code=status.HTTP_418_IM_A_TEAPOT, detail=f"The provided user opinion ID '{userOpinionId}' is not a valid Mongo ID")

    userOpinion = await fetch_user_opinion_by_id(db, userOpinionIdToFetch)
    if userOpinion is not None : 
        return userOpinion

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User opinion {userOpinionId} not found")

@router.post("",response_description="Insert a single user opinion into the DB")
async def add_user_opinion_to_db(userOpinion : UserOpinionStruct = Body(...), db=Depends(get_database)):
    # Check if the user ID is valid
    try:
        userIdToFetch = PyObjectId(userOpinion.userId)
    except:
        raise HTTPException(status_code=status.HTTP_418_IM_A_TEAPOT, detail=f"The provided user ID '{userOpinion.userId}' is not a valid Mongo ID")
    
    # Check if the movie ID is valid
    try:
        movieIdToFetch = PyObjectId(userOpinion.movieId)
    except:
        raise HTTPException(status_code=status.HTTP_418_IM_A_TEAPOT, detail=f"The provided movie ID '{userOpinion.movieId}' is not a valid Mongo ID")

    response = await add_user_opinion(db, userOpinion)
    if response.userOpinionAdded is None:
        if response.error is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{response.error}")
        else:
            raise HTTPException(status_code=status.HTTP_418_IM_A_TEAPOT, detail=f"{response.error}")

    response.userOpinionAdded = str(response.userOpinionAdded)
    
    responseJSON = {"added":response.userOpinionAdded}
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=responseJSON)