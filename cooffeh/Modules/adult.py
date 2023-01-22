from Modules.Adult import xvid, red, hub
from Shared import tools
from requests import get

def run():
    xvid.run()
    hub.run()
    red.run()

def search(term: str):
    xvid.search(term)

def download(link: str):
    content = get(link).content
    if len(content) > tools.megaBytesToBytes(50):
        return ''
    file_ = './Contents/video.mp4'
    with open(file_, 'wb') as f:
        f.write(content)
    return file_
