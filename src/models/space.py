from pydantic import BaseModel
from datetime import date

class SpaceOffer(BaseModel):
    owner: str
    owner_age: int
    telephone: str
    email: str
    type: str
    region: str
    availability_start: str
    availability_end: str
    visitors_max: int
    pet_friendly: bool

class SpaceRequest(BaseModel):
    availability_end: str
    availability_start: str
    pet_friendly: bool
    region: str
    type: str
    visitors_max: int
    
class Space(BaseModel):
    type: str
    region: str
    availability_start: str
    availability_end: str
    visitors_max: int
    pet_friendly: bool
