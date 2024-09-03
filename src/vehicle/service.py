from .schemas import *
from sqlmodel.ext.asyncio.session import AsyncSession
from .repository import VehicleRepository

class VehicleService:
    
    repository = VehicleRepository()

    async def get_all(self, user_uid:str, session: AsyncSession):
        return await self.repository.get_all_by_user_uid(user_uid, session)
    
    async def get_one(self,vehicle_uid:str,user_uid:str, session:AsyncSession):
        vehicle = await self.repository.get_by_uid(vehicle_uid,session)
        if vehicle.user_uid == user_uid or vehicle.showing is True:
            return vehicle

    async def create(self, vehicle_data: VehicleCreateSchema, user_uid: str, session: AsyncSession):
        vehicle_data.user_uid = user_uid

        return await self.repository.create(vehicle_data, session)
    
    async def update(self, vehicle_data: VehicleUpdateSchema, user_uid: str, session:AsyncSession):

        vehicle_saved = await self.repository.get_by_uid_and_user_uid(vehicle_data.uid, user_uid, session)

        return await self.repository.update(vehicle_saved, vehicle_data, session)
    
    async def delete(self, vehicle_uid:str, user_uid:str, session: AsyncSession):
        vehicle = self.repository.get_by_uid_and_user_uid(vehicle_uid,user_uid,session)

        self.repository.delete(vehicle, session)

