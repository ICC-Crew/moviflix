from fastapi import APIRouter, Depends
from ..database.connection import get_database
from ..crud.groups import fetch_groups, fetch_group_by_id, add_group, update_group_in_db, fetch_group_watched_list
from ..models.group import Group,GroupIns,UpdateGroup
from typing import List
from fastapi import HTTPException, Body, status
from fastapi.responses import JSONResponse
from ..models.common import PyObjectId

router = APIRouter(
    prefix="/groups",
    tags=["groups"],
)

@router.get("",response_description="List all groups in DB",response_model=List[Group])
async def get_groups(db = Depends(get_database)): 
    groupList = await fetch_groups(db)
    return groupList

@router.get("/{groupId}",response_description="Find a group with its MongoDB ID",response_model=Group)
async def get_group(groupId:str, db = Depends(get_database)): 
    # Check if the group ID is valid
    try:
        groupIdToFetch = PyObjectId(groupId)
    except:
        raise HTTPException(status_code=status.HTTP_418_IM_A_TEAPOT, detail=f"The provided group ID '{groupId}' is not a valid Mongo ID")
    
    group = await fetch_group_by_id(db,groupIdToFetch)
    if group is not None : 
        return group

    raise HTTPException(status_code=404, detail=f"Group {groupId} not found")

@router.get("/{groupId}/watched",response_description="Find the list of watched movies of a group with its MongoDB ID")
async def get_group_watched_list(groupId:str, db = Depends(get_database)): 
    # Check if the group ID is valid
    try:
        groupIdToFetch = PyObjectId(groupId)
    except:
        raise HTTPException(status_code=status.HTTP_418_IM_A_TEAPOT, detail=f"The provided group ID '{groupId}' is not a valid Mongo ID")
    
    group = await get_group(groupIdToFetch, db)
    
    print(group["members"])

    movieList = await fetch_group_watched_list(db, group["members"])

    raise HTTPException(status_code=404, detail=f"Group {groupId} not found")

@router.post("",response_description="Insert a new group into the DB")
async def insert_group(group:GroupIns = Body(...), db=Depends(get_database)):
    groupId = await add_group(db,group)
    responseJSON = {"insertedId": str(groupId)}
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=responseJSON)

@router.patch("",response_description="Update an existing group of the DB")
async def update_group(groupId:str, group:UpdateGroup, db=Depends(get_database)):
    inserted = await update_group_in_db(db,groupId,group)
    if inserted.updatedGroup is None:
        if inserted.error is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Group {groupId} not found")
        else:
            raise HTTPException(status_code=status.HTTP_418_IM_A_TEAPOT, detail=inserted.error)
    return {"details":inserted}
 