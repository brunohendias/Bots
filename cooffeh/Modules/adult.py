from Modules.cache import Cache
from Modules.Adult import xvid, red, hub
from Models.Video import Video
from Shared import tools
from bs4 import BeautifulSoup as bs
from requests import get

cache = Cache(Video, tools.cacheName('adult'))
def getVideo(index=1):
    return cache.readline(index)

def run():
    xvid.run()
    hub.run()
    red.run()

def download(href, link=''):
    if not link:
        html = get(href).text
        if not html:
            return ''
        soup = bs(html, 'html.parser')
        div = soup.find('div', {'id': 'html5video_base'})
        if not div:
            return 'no link'
        link = div.find('a').attrs['href']
    file_ = './Contents/video.mp4'
    content = get(link).content
    if len(content) > tools.MegaBytesToBytes(50):
        return ''
    with open(file_, 'wb') as f:
        f.write(content)
    return file_
