from Modules.Adult import xvid, red, hub, brasa
from Shared import tools
from requests import get

def run():
    xvid.run()
    hub.run()
    red.run()
    brasa.run()

def search(term: str):
    xvid.search(term)
    red.search(term)
    hub.search(term)
    brasa.search(term)

def download(link: str):
    if not link:
        return ''
    content = get(link).content
    if len(content) > tools.megaBytesToBytes(50):
        return ''
    file_ = './Contents/video.mp4'
    with open(file_, 'wb') as f:
        f.write(content)
    return file_
