from pydantic import BaseModel
from typing import Optional

class VehicleCreateSchema(BaseModel):
    name:str
    brand:str
    model:str
    plate:str
    color:str
    user_uid:Optional[str] = None

class VehicleUpdateSchema(BaseModel):
    uid:str
    name:Optional[str] = None
    brand:Optional[str] = None
    model:Optional[str] = None
    plate:Optional[str] = None
    color:Optional[str] = None