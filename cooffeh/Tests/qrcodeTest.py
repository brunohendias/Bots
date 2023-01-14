from Modules import qrcode_
from Tests.tools import checkIfFileCreated

def testingQRCodeWrite():
    return checkIfFileCreated(
        qrcode_.write('qrcode https://github.com/brunohendias'), 
        'testingQRCodeWrite')
