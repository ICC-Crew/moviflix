from fastapi import APIRouter
import requests
import asyncio

router = APIRouter(
    prefix="/recommandation",
    tags=["recommandation"],
)

FASTAPI_MONGO_URL = "http://moviflix_db-api_1:80/API/v1/"

@router.get("",response_description="Returns the selected fields of all movies")
async def get_movies_with_projection():
    req = requests.get(FASTAPI_MONGO_URL + "movies")
    return req.json()

@router.get("/group_members",response_description="Returns the members of a group")
async def get_group_members(groupId:str):
    req = requests.get(FASTAPI_MONGO_URL + f"groups/{groupId}")
    return req.json()["members"]