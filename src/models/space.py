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
    types: list
    regions: list
    availability_start: date
    availability_end: date
    visitors_min: int
    visitors_max: int
    pet_friendly: bool

class Space(BaseModel):
    type: str
    region: str
    availability_start: date
    availability_end: date
    visitors_min: int
    visitors_max: int
    pet_friendly: bool
