from fastapi import APIRouter, Depends
from ..database.connection import get_database
from ..crud.groups import fetch_groups,fetch_group_by_id,add_group
from ..models.group import Group,GroupIns
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
async def get_group(groupId : str, db = Depends(get_database)): 
    group = await fetch_group_by_id(db,groupId)
    if group is not None : 
        return group

    raise HTTPException(status_code=404, detail=f"Group {groupId} not found")

@router.post("",response_description="Insert a new group into the DB")
async def insert_group(group : GroupIns = Body(...), db=Depends(get_database)):
    groupId = await add_group(db,group)
    responseJSON = {"insertedId": str(groupId)}
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=responseJSON)
 