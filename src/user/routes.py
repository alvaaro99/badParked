from fastapi import APIRouter, status, Depends
from .service import UserService
from .schemas import *
from src.db.database import get_session
from sqlmodel.ext.asyncio.session import AsyncSession
from src.utils.jwt_service import decode_token
from .dependencies import AccessTokenBearer,get_current_user
from src.db.models import User

user_router = APIRouter()
user_service = UserService()
access_token_bearer = AccessTokenBearer()


@user_router.post("/signup", status_code=status.HTTP_201_CREATED)
async def signup(user_data: UserCreateSchema, session: AsyncSession = Depends(get_session)):

    new_user = await user_service.register(user_data,session)
    print(new_user)
    return new_user

@user_router.post("/login", status_code=status.HTTP_200_OK)
async def signup(user_data: UserLoginSchema, session: AsyncSession = Depends(get_session)):
    response = await user_service.login(user_data,session)
    print(response)
    return response

@user_router.put('/update', status_code=status.HTTP_200_OK)
async def update(user_data: UserUpdateSchema, session: AsyncSession = Depends(get_session), user_requesting: User = Depends(get_current_user)):
    return await user_service.update(user_requesting, user_data, session)