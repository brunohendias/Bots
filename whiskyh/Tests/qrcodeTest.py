from Modules.qrcode_ import QRCode
from Tests.tools import checkIfFileCreated

def testingQRCodeWrite():
    file_ = QRCode().write('https://github.com/brunohendias')
    return checkIfFileCreated(file_, 'testingQRCodeWrite')
