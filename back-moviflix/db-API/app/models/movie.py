from typing import Optional, List
from pydantic import BaseModel
from .actor import Actor

class Movie(BaseModel):
    id:str
    fetched:int
    imdbID:str
    title : str
    duration : int
    movieCoverURL : str
    genres : List[str]
    directors : List[str]
    year : int
    synopsis : str
    trailerUrl : str
    moviePicturesURL : List[str]
    actors : List[Actor]

