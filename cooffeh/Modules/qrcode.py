from qrcode import QRCode
from Shared import tools

def write(text):
    qr = QRCode(box_size=4, border=2)
    qr.add_data(text)
    img = qr.make_image()
    file_ = f'./Contents/{tools.fileName()}.jpg'
    return '' if img.save(file_) else file_
