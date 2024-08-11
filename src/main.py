from fastapi import FastAPI
from contextlib import asynccontextmanager
from .db import database

@asynccontextmanager
async def life_span(app:FastAPI):
    print("Starting application!")
    await database.init_db()
    yield
    print("Stopping application!")


app = FastAPI(lifespan=life_span)

@app.get("/")
def read_root():
    return {"Hello": "World"}