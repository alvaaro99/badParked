from datetime import timedelta, datetime
import jwt
import logging
from src.config import Config
import uuid
from itsdangerous import URLSafeTimedSerializer
from src.db.models import User


ACCESS_TOKEN_EXPIRY = 3600
REFRESH_TOKEN_EXPIRY = 3

def create_token(user_data: dict, refresh: bool = False):
    payload = {}

    payload['user'] = user_data
    payload['exp'] = datetime.now() + (
        timedelta(days=REFRESH_TOKEN_EXPIRY) if refresh else timedelta(seconds=ACCESS_TOKEN_EXPIRY)
    )
    payload['jti'] = str(uuid.uuid4())

    payload['refresh'] = refresh

    return jwt.encode(payload=payload,key=Config.JWT_SECRET)


def decode_token(token: str) -> dict:
    try:
        token_decoded = jwt.decode(token,key=Config.JWT_SECRET,algorithms=['HS256'])
    except jwt.PyJWTError as error:
        logging.exception(error)
        return None
    return token_decoded

serializer = URLSafeTimedSerializer(
    secret_key=Config.JWT_SECRET, salt="email-verification"
)

def create_url_safe_token(user: User):
    user_data = {'email':user.email,'fullname':f'{user.name} {user.surname}'}
    token = serializer.dumps(user_data)
    return token

def decode_url_safe_token(token:str):
    try:
        token_data = serializer.loads(token)
        return token_data
    
    except Exception as e:
        logging.error(str(e))
