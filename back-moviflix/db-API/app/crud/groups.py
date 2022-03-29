from fastapi import Query
from ..database.connection import AsyncIOMotorClient
from bson import ObjectId, errors
from ..models.group import GroupIns, UpdateGroup, UpdateStructure
from ..crud.users import fetch_user_by_id
from typing import List
from ..models.common import PyObjectId

database_name = "moviflixDB"
collection_name= "groups"

async def fetch_groups(conn: AsyncIOMotorClient):
    row = await conn[database_name][collection_name].find().to_list(length=1000)
    return row

async def fetch_group_by_id(conn: AsyncIOMotorClient,groupId:str):
    row = await conn[database_name][collection_name].find_one({"_id": ObjectId(groupId)}) 
    return row    

async def add_group(conn : AsyncIOMotorClient, group:GroupIns):
    groupDict = GroupIns(**group.dict())
    newGroup = await conn[database_name][collection_name].insert_one(groupDict.dict())
    return newGroup.inserted_id

async def update_group_in_db(conn : AsyncIOMotorClient, groupId:str, group:UpdateGroup):
    return_structure = UpdateStructure()

    groupDict = UpdateGroup(**group.dict(exclude_unset=True))
    
    # Verify the validity of the group ID
    try:
        groupIdToFetch = PyObjectId(groupId)
    except errors.InvalidId:
        return_structure.error = f"Error: groupId {groupId} is not a valid Mongo ID"
        return return_structure
    
    groupToUpdate = await fetch_group_by_id(conn, groupId)
    
    # Group ID not found
    if groupToUpdate is None:
        return return_structure

    groupToUpdate = GroupIns(**groupToUpdate)


    # Updating the fields
    if groupDict.groupName != None:
        if groupDict.groupName == "":
            return_structure.error = "The group name cannot be empty"
            return return_structure
        else:
            groupToUpdate.groupName = groupDict.groupName
    
    if groupDict.admin != None:
        # Check if the user ID is valid
        try:
            userIdToProcess = PyObjectId(groupDict.admin)
        except:
            return_structure.error = f"The provided user ID '{groupDict.admin}' is not a valid Mongo ID"
            return return_structure

        groupToUpdate.admin = userIdToProcess
    

    if groupDict.operation is not None:
        # Check if the user ID is valid
        try:
            userIdToProcess = PyObjectId(groupDict.operation.userID)
        except:
            return_structure.error = f"The provided user ID '{groupDict.operation.userID}' is not a valid Mongo ID"
            return return_structure

        if groupDict.operation.operationType == "add":
            if userIdToProcess not in groupToUpdate.members:
                # Check if user exists
                userInDB = await fetch_user_by_id(conn, groupDict.operation.userID)

                if userInDB is not None:
                    groupToUpdate.members.append(userIdToProcess)
                else:
                    return_structure.error = f"The provided user '{groupDict.operation.userID}' does not exist in the database"

        elif groupDict.operation.operationType == "remove":
            if str(userIdToProcess) == groupToUpdate.admin:
                return_structure.error = f"The provided user '{userIdToProcess}' cannot be removed because he is the administrator of this group"
            else:
                if userIdToProcess in groupToUpdate.members:
                    groupToUpdate.members.remove(userIdToProcess)
                else:
                    return_structure.error = f"The provided user '{userIdToProcess}' cannot be removed because he is not present in this group"

        else:
            return_structure.error = f"Provided operation type '{groupDict.operation.operationType}' is invalid (available: 'add', 'remove')"
    
    if return_structure.error is not None:
        return_structure.updatedGroup = None
    else:
        response = await conn[database_name][collection_name].update_one({"_id": ObjectId(groupId)}, {"$set": groupToUpdate.dict()})
        if response:
            res = f"{groupToUpdate}"
        else:
            res = None
        return_structure.updatedGroup = res
        
    return return_structure