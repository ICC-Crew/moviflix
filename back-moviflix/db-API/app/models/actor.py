from pydantic import BaseModel

class Actor(BaseModel):
    name : str
    asCharacter : str
    imgActorUrl : str
