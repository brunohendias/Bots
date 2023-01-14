from Modules import youtube
from Tests.tools import checkIfFileCreated, msg

def testingYoutubeDownloadVideo():
    return checkIfFileCreated(
        youtube.download('https://www.youtube.com/watch?v=tPEE9ZwTmy0'), 
        'testingYoutubeDownloadVideo')
