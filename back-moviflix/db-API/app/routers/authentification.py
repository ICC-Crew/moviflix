from fastapi import APIRouter, Depends
from ..database.connection import get_database
from ..crud.users import fetch_login_user_name_and_pwd
from ..models.user import UserLogin
from fastapi import HTTPException, Body, status
from fastapi.responses import JSONResponse
from app.models.model import PostSchema

router = APIRouter(
     prefix="/auth",
    tags=["auth"],
)


posts = [
    {
        "id": 1,
        "title": "Pancake",
        "content": "Lorem Ipsum ..."
    }
]

users = []


@router.get("/test",tags=["gets"])
async def read_root() -> dict:
    return {"message": "Welcome to your blog!."}


@router.get("/posts", tags=["gets"])
async def get_posts() -> dict:
    return { "data": posts }


@router.get("/posts/{id}", tags=["gets"])
async def get_single_post(id: int) -> dict:
    if id > len(posts):
        return {
            "error": "No such post with the supplied ID."
        }

    for post in posts:
        if post["id"] == id:
            return {
                "data": post
            }

@router.post("/posts", tags=["posts"])
async def add_post(post: PostSchema) -> dict:
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {
        "data": "post added."
    }

@router.post("/login",response_description="Login user with its username+pwd")
async def login_user_by_username_pwd(user : UserLogin = Body(...), db = Depends(get_database)): 
    response = await fetch_login_user_name_and_pwd(db,user)
    if response is not None : 
        return {"msg" : "You are logged in !"}

    raise HTTPException(status_code=404, detail=f"Username or password is wrong, retry.")

