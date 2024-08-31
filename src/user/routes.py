from fastapi import APIRouter, status, Depends, BackgroundTasks
from .service import UserService
from .schemas import *
from src.db.database import get_session
from sqlmodel.ext.asyncio.session import AsyncSession
from src.utils.jwt_service import decode_token
from .dependencies import AccessTokenBearer,get_current_user
from src.db.models import User
from src.utils import mail_service
from src.config import Config
from fastapi.responses import JSONResponse
from src.utils.jwt_service import create_token, create_url_safe_token, decode_url_safe_token


user_router = APIRouter()
user_service = UserService()
access_token_bearer = AccessTokenBearer()

@user_router.get('/verify/{url_token}', status_code=status.HTTP_200_OK)
async def verify(url_token: str, session: AsyncSession = Depends(get_session)):
    token_data: dict = decode_url_safe_token(url_token)
    user_to_verify = UserVerifySchema(email=token_data.get('email'))
    return await user_service.verify(user_to_verify, session)


@user_router.post("/signup", status_code=status.HTTP_201_CREATED)
async def signup(user_data: UserCreateSchema, bg_tasks: BackgroundTasks, session: AsyncSession = Depends(get_session)):

    new_user = await user_service.register(user_data,session)

    url_token = create_url_safe_token(new_user)

    bg_tasks.add_task(mail_service.send_verification_mail, new_user, f'{Config.DOMAIN}/api/user/verify/{url_token}')

    response = generate_data_token(new_user, 'Register Succesfull')

    return response

@user_router.post("/login", status_code=status.HTTP_200_OK)
async def signup(user_data: UserLoginSchema, session: AsyncSession = Depends(get_session)):
    user = await user_service.login(user_data,session)
    response = generate_data_token(user,'Login Succesfull')
    return response

@user_router.put('/update', status_code=status.HTTP_200_OK)
async def update(user_data: UserUpdateSchema, session: AsyncSession = Depends(get_session), user_requesting: User = Depends(get_current_user)):
    user = await user_service.update(user_requesting, user_data, session)
    response = generate_data_token(user,'Update Succesfull')
    return response


@user_router.delete('/delete', status_code=status.HTTP_200_OK)
async def delete(session: AsyncSession = Depends(get_session), user: User = Depends(get_current_user)):
    return await user_service.delete(user, session)


def generate_data_token(user: User, message: str = 'Ok'):
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