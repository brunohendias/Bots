from qrcode import QRCode

def write(text):
    qr = QRCode(box_size=4, border=2)
    qr.add_data(text)
    img = qr.make_image()
    file_ = './Contents/qrcode.jpg'
    return '' if img.save(file_) else file_
