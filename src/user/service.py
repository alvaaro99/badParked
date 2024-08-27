from src.db.models import User
from fastapi.responses import JSONResponse
from .schemas import *
from .password_service import verify_password
from .repository import UserRepository
from sqlmodel.ext.asyncio.session import AsyncSession
from src.utils.jwt_service import create_token
class UserService:

    repository = UserRepository()

    async def register(self, user_data: UserCreateSchema, session: AsyncSession):
        user = await self.repository.create_user(user_data,session)

        return self.generate_data_token(user, 'Register Succesfull')



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
        user_updated = await self.repository.update_user(user_in_db, user_data, session)

        return self.generate_data_token(user_updated, 'Update Succesfull')
    
    async def delete(self, user: User, session: AsyncSession) -> bool:
        #if not 
        return await self.repository.delete_user(user.uid, session)
            #TODO: raise exception

    def generate_data_token(self, user: User, message: str = 'Ok'):
        user_data = {'email':user.email,'fullname':f'{user.name} {user.surname}'}
        access_token = create_token(user_data)
        refresh_token = create_token(user_data,refresh=True)

        return JSONResponse(
            content = {
                'message':message,
                'access_token':access_token,
                'refresh_token':refresh_token
            }
        )