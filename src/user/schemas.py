from pydantic import BaseModel

class UserCreateSchema(BaseModel):
    name:str
    surname:str
    email:str
    password:str

class UserUpdateSchema(BaseModel):
    name:str
    surname:str
    email:str
    password:str
    is_verified:bool
