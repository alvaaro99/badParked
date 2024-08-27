from src.db.models import Vehicle
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from .schemas import *
from typing import Sequence

class VehicleRepository:

    async def create(self, vehicle: VehicleCreateSchema, session: AsyncSession) -> Vehicle:
        new_vehicle = Vehicle(**vehicle.model_dump())
        session.add(new_vehicle)
        await session.commit()

        return new_vehicle
    

    async def get_by_uid(self, vehicle_uid:str, session: AsyncSession) -> Vehicle:
        query = select(Vehicle).where(Vehicle.uid == vehicle_uid)

        vehicles = await session.exec(query)

        return vehicles.first()
    
    async def get_by_uid_and_user_uid(self, vehicle_uid:str, user_uid:str, session: AsyncSession) -> Vehicle:
        query = select(Vehicle).where(Vehicle.uid == vehicle_uid).where(Vehicle.user_uid == user_uid)

        vehicles = await session.exec(query)

        return vehicles.first()


    async def get_all_by_user_uid(self, user_uid: str, session: AsyncSession) -> Sequence[Vehicle]:

        query = select(Vehicle).where(Vehicle.user_uid == user_uid)
        vehicles = await session.exec(query)

        return vehicles.all()
    

    async def delete(self, vehicle_uid: str, session: AsyncSession):

        query = select(Vehicle).where(Vehicle.uid == vehicle_uid)
        result = await session.exec(query)
        vehicle = result.first()

        if vehicle is not None:
            await session.delete(vehicle)

    
    async def update(self, vehicle_saved: Vehicle, vehicle_data: VehicleUpdateSchema, session: AsyncSession) -> Vehicle:

        for key, value in vehicle_data.model_dump().items():
            if value is not None:
                setattr(vehicle_saved,key,value)

        await session.commit()

        return vehicle_saved

