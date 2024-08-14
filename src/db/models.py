from typing import List 
from sqlmodel import Field, SQLModel, Relationship, Column
import sqlalchemy.dialects.postgresql as pg
import uuid

class User(SQLModel, table=True):
    __tablename__ = "users"
    uid: uuid.UUID = Field(
        sa_column=Column(pg.UUID , nullable=False, primary_key=True, default=uuid.uuid4)
    )    
    email: str = Field(sa_column=Column(pg.VARCHAR, nullable=False, unique=True))
    name: str
    surname: str
    password: str
    is_verified: bool = Field(default=False)

    vehicles: List["Vehicle"] = Relationship(back_populates="user", sa_relationship_kwargs={"lazy": "selectin"}) 

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
    user: User = Relationship(back_populates="vehicles")  