from multiprocessing.dummy import Array
from pydantic import BaseModel, Field
from .common import PyObjectId
from bson import ObjectId
from typing import List
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