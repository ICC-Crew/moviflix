from fastapi import APIRouter, HTTPException, status
import requests
import asyncio
from ..models.common import PyObjectId
import random

router = APIRouter(
    prefix="/recommandation",
    tags=["recommandation"],
)

FASTAPI_MONGO_URL = "http://moviflix_db-api_1:80/API/v1/"

@router.get("",response_description="Return the selected fields of all movies (title and cover by default)")
async def get_movies_with_projection(limit:int = 20, page:int = 0, parameters:str = ""):
    req = requests.get(FASTAPI_MONGO_URL + f"movies?limit={limit}&page={page}&parameters={parameters}")
    return req.json()

@router.get("/group_members",response_description="Returns the members of a group")
async def get_group_members(groupId:str, token:str):
    # Check if the group ID is valid
    try:
        groupIdToFetch = PyObjectId(groupId)
    except:
        raise HTTPException(status_code=status.HTTP_418_IM_A_TEAPOT, detail=f"The provided group ID '{groupId}' is not a valid Mongo ID")

    req = requests.get(FASTAPI_MONGO_URL + f"groups/{groupId}", headers={"Authorization": f"Bearer {token}"})

    if ("members" in req.json()):
        return{"members": req.json()["members"]} 
    else:
        return req.json()
        

@router.get("/get_recommandation", response_description="Return a movie suggestion based on the genres of the movies watched by the group")
async def get_recommandation(groupId:str, token:str):
    # Check if the group ID is valid
    try:
        groupIdToFetch = PyObjectId(groupId)
    except:
        raise HTTPException(status_code=status.HTTP_418_IM_A_TEAPOT, detail=f"The provided group ID '{groupId}' is not a valid Mongo ID")

    # Group members
    groupResponse = requests.get(FASTAPI_MONGO_URL + f"groups/{groupId}", headers={"Authorization": f"Bearer {token}"})
    if groupResponse.status_code != 200 or "members" not in groupResponse.json():
        raise HTTPException(status_code=status.HTTP_418_IM_A_TEAPOT, detail=f"{groupResponse}")

    groupMembers = groupResponse.json()["members"]

    # Movies watched by the group
    movieResponse = requests.get(FASTAPI_MONGO_URL + f"groups/{groupId}/watched", headers={"Authorization": f"Bearer {token}"})
    if movieResponse.status_code != 200:
        raise HTTPException(status_code=status.HTTP_418_IM_A_TEAPOT, detail=f"{movieResponse}")

    watchedMovieGenres = [el["genres"] for el in movieResponse.json()]
    watchedMovieIds = [el["_id"] for el in movieResponse.json()]

    genresToQueryDict = {}
    for genres in watchedMovieGenres:
        for genre in genres:
            if genre not in genresToQueryDict:
                genresToQueryDict[genre] = 0
        
            genresToQueryDict[genre] += 1
    
    genresToQuery = ""
    for genre in genresToQueryDict:
        genresToQuery += f"{genre},"
    
    movieIdsToQuery = ""
    for movieId in watchedMovieIds:
        movieIdsToQuery += f"{movieId},"

    # Movie suggestion based on genre
    movieResponse = requests.get(FASTAPI_MONGO_URL + f"movies/filter?genres={genresToQuery[:-1]}&exclude={movieIdsToQuery[:-1]}")

    AIBasedSuggestionIndex = random.randint(0, len(movieResponse.json()["movies"]))

    return movieResponse.json()["movies"][AIBasedSuggestionIndex]