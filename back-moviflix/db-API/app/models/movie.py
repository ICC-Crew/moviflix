from typing import Optional, List
from pydantic import BaseModel, Field
from .actor import Actor
from .common import PyObjectId
from bson import ObjectId

class Movie(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    fetched:int
    imdbID:str
    title : str
    duration : Optional[int]
    movieCoverUrl : Optional[str]
    genres : Optional[List[str]]
    directors : Optional[List[str]]
    year : Optional[int]
    synopsis : Optional[str]
    trailerUrl : Optional[str]
    moviePicturesURL : Optional[List[str]]
    actors : Optional[List[Actor]]
        
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}