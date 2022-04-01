from pydantic import BaseModel, Field, EmailStr
from .common import PyObjectId
from bson import ObjectId



class User(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    userName : str = Field(...)
    password : str = Field(...)
    email : EmailStr = Field(...)

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class UserIns(BaseModel):
    userName : str = Field(...)
    password : str = Field(...)
    email : EmailStr = Field(...)
    
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class UpdateStructureUser(BaseModel):
    userAdded : UserIns = None
    error : str = None


class UserLoginSchema(BaseModel):
    userName: str = Field(...)
    password: str = Field(...)

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
