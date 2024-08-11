from typing import List 
from sqlmodel import Field, SQLModel, Relationship, Column
import sqlalchemy.dialects.postgresql as pg
import uuid

class User(SQLModel, table=True):
    __tablename__ = "users"
    uid: uuid.UUID = Field(
        sa_column=Column(pg.UUID , nullable=False, primary_key=True, default=uuid.uuid4)
    )    
    email: str
    name: str
    surname: str
    password: str
    is_verified: bool = Field(default=False)

    vehicles: List["Vehicle.Vehicle"] = Relationship(back_populates="user") 

class Vehicle(SQLModel, table=True):
    __tablename__ = 'vehicles'
    uid: uuid.UUID = Field(
        sa_column=Column(pg.UUID, nullable=False, primary_key=True, default=uuid.uuid4)
    )
    brand: str
    model: str
    name: str
    plate: str

    user_uid: uuid.UUID = Field(foreign_key="users.uid")
    user: "User.User" = Relationship(back_populates="vehicles")  