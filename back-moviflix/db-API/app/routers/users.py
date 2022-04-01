from fastapi import APIRouter, Depends
from ..database.connection import get_database
from ..crud.users import fetch_users,fetch_user_by_id,fetch_user_by_user_name
from ..models.user import User
from typing import List
from fastapi import HTTPException, Body, status
from ..models.common import PyObjectId
from app.auth.auth_bearer import JWTBearer

router = APIRouter(
     prefix="/users",
    tags=["users"],
)

@router.get("",dependencies=[Depends(JWTBearer())],response_description="List all users in DB",response_model=List[User])
async def get_users(db = Depends(get_database)): 
    userList = await fetch_users(db)
    return userList

@router.get("/{userId}", dependencies=[Depends(JWTBearer())], response_description="Find an user with its MongoDB ID",response_model=User)
async def get_user(userId : str, db = Depends(get_database)):
    # Check if the user ID is valid
    try:
        userIdToFetch = PyObjectId(userId)
    except:
        raise HTTPException(status_code=status.HTTP_418_IM_A_TEAPOT, detail=f"The provided user ID '{userId}' is not a valid Mongo ID")

    user = await fetch_user_by_id(db,userIdToFetch)
    if user is not None : 
        return user

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User {userId} not found")

@router.get("/username/{userName}", dependencies=[Depends(JWTBearer())], response_description="Find an user with its username",response_model=User)
async def get_user_by_username(userName : str, db = Depends(get_database)): 
    user = await fetch_user_by_user_name(db,userName)
    if user is not None : 
        return user

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User {userName} not found")
 