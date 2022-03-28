from pydantic import BaseModel, Field
from .common import PyObjectId
from bson import ObjectId



class User(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    userName : str
    password : str
    email : str

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class UserIns(BaseModel):
    userName : str
    password : str
    email : str
    
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}