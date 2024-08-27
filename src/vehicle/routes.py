from fastapi import APIRouter, status, Depends
from .service import VehicleService
from .schemas import *
from src.db.database import get_session
from src.db.models import User
from sqlmodel.ext.asyncio.session import AsyncSession
from src.user.dependencies import get_current_user

vehicle_router = APIRouter()
vehicle_service = VehicleService()


@vehicle_router.get('/', status_code=status.HTTP_200_OK)
async def get_all(session: AsyncSession = Depends(get_session), user: User = Depends(get_current_user)):
    return await vehicle_service.get_all(user.uid, session)

@vehicle_router.get('/{vehicle_uid}', status_code=status.HTTP_200_OK)
async def get_one(vehicle_uid:str, session: AsyncSession = Depends(get_session), user: User = Depends(get_current_user)):
    return await vehicle_service.get_one(vehicle_uid, user.uid, session)

@vehicle_router.post("/create", status_code=status.HTTP_201_CREATED)
async def new_vehicle(vehicle_data: VehicleCreateSchema, session: AsyncSession = Depends(get_session), user: User = Depends(get_current_user)):
    new_vehicle = await vehicle_service.create(vehicle_data,user.uid,session)
    return new_vehicle

@vehicle_router.put("/update", status_code=status.HTTP_200_OK)
async def new_vehicle(vehicle_data: VehicleUpdateSchema, session: AsyncSession = Depends(get_session), user: User = Depends(get_current_user)):

    vehicle_updated = await vehicle_service.update(vehicle_data,user.uid,session)
    return vehicle_updated

@vehicle_router.delete('/{vehicle_uid}', status_code=status.HTTP_200_OK)
async def delete_vehicle(vehicle_uid:str, session: AsyncSession = Depends(get_session), user: User = Depends(get_current_user)):
    await vehicle_service.delete(vehicle_uid, user.uid, session)