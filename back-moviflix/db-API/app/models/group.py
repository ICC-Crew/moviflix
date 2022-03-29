from multiprocessing.dummy import Array
from tokenize import group
from pydantic import BaseModel, Field
from .common import PyObjectId
from bson import ObjectId
from typing import List, Optional
from .user import User

class Group(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    groupName : str
    admin : PyObjectId
    members : List[PyObjectId]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class GroupIns(BaseModel):
    groupName : str
    admin : PyObjectId
    members : List[PyObjectId]

    class Config:   
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class Operation(BaseModel):
    operationType : str
    userID : str

class UpdateGroup(BaseModel):
    groupName : Optional[str] = None
    admin : Optional[str] = None
    operation : Optional[Operation] = None

    class Config:   
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        
class UpdateStructure(BaseModel):
    updatedGroup : Group = None
    error : str = None