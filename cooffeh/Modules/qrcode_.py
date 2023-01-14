from qrcode import QRCode as Code

class QRCode:
    def write(self, content):
        qr = Code(box_size=5, border=2)
        qr.add_data(content)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        file_ = './Contents/qrcode.jpg'
        img.save(file_)
        return file_

def write(text):
    return QRCode().write(text.split(' ')[1])