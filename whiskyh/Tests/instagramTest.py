from Modules.instagram import Instagram
from Tests.tools import checkIfFileCreated, msg

def checkIfFailedDownloadPostNotFound():
    msg.text = 'https://www.instagram.com/p/CnAbf4x'
    file_ = Instagram().downloadImagePost(msg)
    if not file_:
        return 200
    return 'checkIfFailedDownloadPostNotFound failed'

def testingInstagramDownloadImagePost():
    msg.text = 'https://www.instagram.com/p/CnAbf4xO35M'
    file_ = Instagram().downloadImagePost(msg)
    return checkIfFileCreated(file_, 'testingInstagramDownloadImagePost')