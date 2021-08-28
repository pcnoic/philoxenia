from pydantic import BaseModel
from datetime import datetime

class SpaceOffer(BaseModel):
    owner: str
    owner_age: int
    type: str
    region: str
    availability_start: datetime.date
    availability_end: datetime.date
    date_added: datetime.date
    visitors_max: int
    pet_friendly: bool

class SpaceRequest(BaseModel):
    types: list
    regions: list
    availability_start: datetime.date
    availability_end: datetime.date
    visitors_min: int
    visitors_max: int
    pet_friendly: bool

class Space(BaseModel):
    type: str
    region: str
    availability_start: datetime.date
    availability_end: datetime.date
    visitors_min: int
    visitors_max: int
    pet_friendly: bool
