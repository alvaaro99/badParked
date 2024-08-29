from src.db.models import User
from .schemas import *
from .password_service import verify_password
from .repository import UserRepository
from sqlmodel.ext.asyncio.session import AsyncSession
class UserService:

    repository = UserRepository()

    async def register(self, user_data: UserCreateSchema, session: AsyncSession):
        return await self.repository.create_user(user_data,session)



    async def login(self, user_data: UserLoginSchema, session: AsyncSession) -> User:
        user: User = await self.repository.get_user_by_email(user_data.email,session)
        if user is None:
            #TODO: raise NotFound
            return None
        if not verify_password(user_data.password,user.password):
            # TODO: raise Incorrect
            return None
        
        return self.generate_data_token(user, 'Login Succesfull')

    

    async def update(self, user_in_db: User, user_data: UserUpdateSchema, session: AsyncSession) -> User:
        return await self.repository.update_user(user_in_db, user_data, session)
    
    async def delete(self, user: User, session: AsyncSession) -> bool:
        #if not 
        return await self.repository.delete_user(user.uid, session)
            #TODO: raise exception
