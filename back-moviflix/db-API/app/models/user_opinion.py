from pydantic import BaseModel, Field
from .common import PyObjectId
from bson import ObjectId



class UserOpinion(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    movieId : PyObjectId
    userId : PyObjectId
    rating : int

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class UserOpinionIns(BaseModel):
    movieId : PyObjectId
    userId : PyObjectId
    rating : int
    
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class UserOpinionStruct(BaseModel):
    movieId : str
    userId : str
    rating : int = 1
    
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class UpdateStructureUserOpinion(BaseModel):
    userOpinionAdded : UserOpinionIns = None
    error : str = None
