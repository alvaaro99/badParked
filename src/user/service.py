from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from src.db.models import User
from .schemas import *

class UserService:

    async def get_user_by_uid(self, user_uid:str, session: AsyncSession):
        query = select(User).where(User.uid == user_uid)

        result = await session.exec(query)
        return result.first()
    
    async def get_user_by_email(self, user_email:str, session: AsyncSession):
        query = select(User).where(User.email == user_email)

        result = await session.exec(query)
        return result.first()

    async def create_user(self, user_data: UserCreateSchema, session: AsyncSession):
        new_user = User(**user_data.model_dump())

        session.add(new_user)
        await session.commit()

        return new_user

    async def update_user(self, user_uid: str, user_data: UserUpdateSchema, session: AsyncSession):
        user_to_update: User = await self.get_user(user_uid)

        for key, value in user_data.model_dump().items():
            setattr(user_to_update,key,value)

        await session.commit()

        return user_to_update
    
    async def delete_user(self, user_uid: str, session: AsyncSession):
        user_to_delete = await self.get_user(user_uid, session)
        if user_to_delete is not None:
            await session.delete(user_to_delete)
            await session.commit()

            return 'Deleted'
        return None