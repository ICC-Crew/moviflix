from fastapi import APIRouter, Depends
from ..database.connection import get_database
from ..crud.users import fetch_login_user_name_and_pwd
from ..models.user import UserLogin
from fastapi import HTTPException, Body, status
from fastapi.responses import JSONResponse

router = APIRouter(
     prefix="/auth",
    tags=["auth"],
)

@router.post("/login",response_description="Login user with its username+pwd")
async def login_user_by_username_pwd(user : UserLogin = Body(...), db = Depends(get_database)): 
    response = await fetch_login_user_name_and_pwd(db,user)
    if response is not None : 
        return {"msg" : "You are logged in !"}

    raise HTTPException(status_code=404, detail=f"Username or password is wrong, retry.")