import qrcode
from src.db.models import Vehicle
from src.config import Config
import os

def generate_qrcode(vehicle: Vehicle):
    url = f'{Config.DOMAIN}/api/vehicle/{vehicle.uid}'
    path = f'./qr-codes/{vehicle.uid}.png'

    if not is_qr_already_generated(path):
        qr_image = qrcode.make(url)
        qr_image.save(path)

    return path



def is_qr_already_generated(path_qr: str):

    if os.path.exists(path_qr):
        return True
    return False