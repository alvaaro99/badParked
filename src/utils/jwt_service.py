from datetime import timedelta, datetime
import jwt
import logging
from src.config import Config
import uuid


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
