from fastapi import FastAPI
from contextlib import asynccontextmanager
from .db import database
from .user.routes import user_router
from .vehicle.routes import vehicle_router

@asynccontextmanager
async def life_span(app:FastAPI):
    print("Starting application!")
    await database.init_db()
    yield
    print("Stopping application!")


app = FastAPI(lifespan=life_span)

app.include_router(user_router,prefix='/api/user', tags=['user'])
app.include_router(vehicle_router, prefix='/api/vehicle',tags=['vehicle'])