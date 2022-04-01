from fastapi import APIRouter, Depends
from ..database.connection import get_database
from ..crud.users import fetch_check_exist_user_login, add_user
from ..models.user import UserIns, UserLoginSchema
from fastapi import HTTPException, Body, status
from app.auth.auth_handler import signJWT
from app.auth.auth_bearer import JWTBearer

router = APIRouter(
     prefix="/auth",
    tags=["auth"],
)


@router.post("/user/register", response_description="Insert a single user into the DB")
async def user_register(user: UserIns = Body(...), db = Depends(get_database)):
    response = await add_user(db,user)
    if response.userAdded is None:
        if response.error is not None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{response.error}")
    # responseJSON = {"msg":response.userAdded}
    # return JSONResponse(status_code=status.HTTP_201_CREATED, content=responseJSON)
    # users.append(user) # replace with db call, making sure to hash the password first
    return signJWT(user.userName)


@router.post("/user/login", response_description="Try login an user")
async def user_login(user: UserLoginSchema = Body(...), db = Depends(get_database)):
    response = await fetch_check_exist_user_login(db,user)
    print("repsonse",response)
    if response is True:
        return signJWT(user.userName)
    raise HTTPException(status_code=404, detail=f"Username or password is wrong, retry.")
