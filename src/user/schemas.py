from pydantic import BaseModel
from typing import Optional

class UserCreateSchema(BaseModel):
    name:str
    surname:str
    email:str
    password:str

class UserLoginSchema(BaseModel):
    email:str
    password:str

class UserUpdateSchema(BaseModel):
    name:Optional[str] = None
    surname:Optional[str] = None
    email:Optional[str] = None
    password:Optional[str] = None
    is_verified:Optional[bool] = None
