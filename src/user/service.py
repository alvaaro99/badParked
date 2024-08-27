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

        user_data = {'email':user.email,'fullname':f'{user.name} {user.surname}'}
        access_token = create_token(user_data)
        refresh_token = create_token(user_data,refresh=True)

        return JSONResponse(
            content = {
                'message':'Registered successfull',
                'access_token':access_token,
                'refresh_token':refresh_token
            }
        )


    async def login(self, user_data: UserLoginSchema, session: AsyncSession) -> User:
        user: User = await self.repository.get_user_by_email(user_data.email,session)
        if user is None:
            #TODO: raise NotFound
            return None
        if not verify_password(user_data.password,user.password):
            # TODO: raise Incorrect
            return None
        user_data = {'email':user.email,'fullname':f'{user.name} {user.surname}'}
        access_token = create_token(user_data)
        refresh_token = create_token(user_data,refresh=True)

        return JSONResponse(
            content = {
                'message':'Login successfull',
                'access_token':access_token,
                'refresh_token':refresh_token
            }
        )
    

    async def update(self, user_in_db: User, user_data: UserUpdateSchema, session: AsyncSession) -> User:
        user_updated = await self.repository.update_user(user_in_db, user_data, session)

        user_data = {'email':user_updated.email,'fullname':f'{user_updated.name} {user_updated.surname}'}
        access_token = create_token(user_data)
        refresh_token = create_token(user_data,refresh=True)

        return JSONResponse(
            content = {
                'message':'Updated successfull',
                'access_token':access_token,
                'refresh_token':refresh_token
            }
        )
    
    async def delete(self, user: User, session: AsyncSession) -> bool:
        #if not 
        return await self.repository.delete_user(user.uid, session)
            #TODO: raise exception
