from Modules import instagram
from Tests.tools import checkIfFileCreated, msg

def checkIfFailedDownloadPostNotFound():
    file_ = instagram.download('https://www.instagram.com/p/CnAbf4x')
    if not file_:
        return 200
    return 'checkIfFailedDownloadPostNotFound failed'

def testingInstagramDownloadImagePost():
    return checkIfFileCreated(
        instagram.download('https://www.instagram.com/p/CnAbf4xO35M'),
        'testingInstagramDownloadImagePost')
