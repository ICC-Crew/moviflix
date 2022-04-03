from fastapi import APIRouter
import requests
import asyncio

router = APIRouter(
    prefix="/recommandation",
    tags=["recommandation"],
)

FASTAPI_MONGO_URL = "http://moviflix_db-api_1:80/API/v1/"

@router.get("",response_description="Returns the selected fields of all movies (title and cover by default)")
async def get_movies_with_projection(limit:int = 20, page:int = 0, parameters:str = ""):
    req = requests.get(FASTAPI_MONGO_URL + f"movies?limit={limit}&page={page}&parameters={parameters}")
    return req.json()

@router.get("/group_members",response_description="Returns the members of a group")
async def get_group_members(groupId:str):
    req = requests.get(FASTAPI_MONGO_URL + f"groups/{groupId}")
    return req.json()["members"]