from qrcode import QRCode

def write(text):
    qr = QRCode(box_size=5, border=2)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    file_ = './Contents/qrcode.jpg'
    img.save(file_)
    return file_
