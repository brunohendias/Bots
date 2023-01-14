from Modules.youtube import Youtube
from Tests.tools import checkIfFileCreated, msg

def testingYoutubeDownloadVideo():
    msg.text = 'https://www.youtube.com/watch?v=tPEE9ZwTmy0'
    file_ = Youtube().downloadVideo(msg)
    return checkIfFileCreated(file_, 'testingYoutubeDownloadVideo')