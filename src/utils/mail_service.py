from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from src.config import Config
from src.db.models import User

conf = ConnectionConfig(
    MAIL_USERNAME = Config.MAIL_USERNAME,
    MAIL_PASSWORD = Config.MAIL_PASSWORD,
    MAIL_FROM = Config.MAIL_FROM,
    MAIL_PORT = Config.MAIL_PORT,
    MAIL_SERVER = Config.MAIL_SERVER,
    MAIL_FROM_NAME= Config.MAIL_FROM_NAME,
    MAIL_STARTTLS = True,
    MAIL_SSL_TLS = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)

async def send_verification_mail(user: User, link: str):
    html = f'<p>Thank you for register on BadParking! Please verify your account: {link}</p>'

    message = MessageSchema(
        subject="BadParking New User",
        recipients=[user.email],
        body=html,
        subtype=MessageType.html)

    fm = FastMail(conf)
    await fm.send_message(message)