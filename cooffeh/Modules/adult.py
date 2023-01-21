from Modules.Adult import xvid, red, hub
from Shared import tools
from requests import get

def run():
    xvid.run()
    hub.run()
    red.run()

def download(link):
    if not link:
        return ''
    file_ = './Contents/video.mp4'
    content = get(link).content
    if len(content) > tools.MegaBytesToBytes(50):
        return ''
    with open(file_, 'wb') as f:
        f.write(content)
    return file_
