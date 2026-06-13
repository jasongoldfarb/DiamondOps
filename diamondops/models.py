
from dataclasses import dataclass

@dataclass
class Hotel:
    id:int
    name:str
    address:str
    lat:float|None=None
    lng:float|None=None

@dataclass
class Team:
    id:int
    name:str
    seed:int
    hotel_id:int

@dataclass
class Field:
    id:int
    name:str
    address:str
    active:bool=True
    lat:float|None=None
    lng:float|None=None
