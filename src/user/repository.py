from src.db.models import User
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from .password_service import generate_hash_password
from .schemas import *

class UserRepository():

    async def create_user(self, user_data: UserCreateSchema, session: AsyncSession) -> User:
        new_user = User(**user_data.model_dump())

        new_user.password = generate_hash_password(new_user.password)

        session.add(new_user)
        await session.commit()

        return new_user

    async def get_user_by_uid(self, user_uid:str, session: AsyncSession) -> User:
        query = select(User).where(User.uid == user_uid)

        result = await session.exec(query)
        return result.first()
    
    async def get_user_by_email(self, user_email:str, session: AsyncSession) -> User:
        query = select(User).where(User.email == user_email)

        result = await session.exec(query)
        return result.first()
    
    async def delete_user(self, user_uid: str, session: AsyncSession) -> bool:
        user_to_delete = await self.get_user_by_uid(user_uid, session)
        if user_to_delete is not None:
            await session.delete(user_to_delete)
            await session.commit()

            return True
        return False

    async def update_user(self, user_saved: User, user_data: UserUpdateSchema, session: AsyncSession) -> User:
        

        for key, value in user_data.model_dump().items():
            if value is not None:
                setattr(user_saved,key,value)

        await session.commit()

        return user_saved