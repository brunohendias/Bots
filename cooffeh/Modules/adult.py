from Modules.cache import Cache
from Modules.Adult import red, hub
from Models.Video import Video
from Shared import tools
from bs4 import BeautifulSoup as bs
from requests import get
from os import stat

basepath = 'https://www.xvideos.com'
cache = Cache(Video, tools.cacheName('adult'))

def getVideo(index=1):
    return cache.readline(index)

def run():
    cache.delOld()
    html = get(basepath).text
    soup = bs(html, 'html.parser')
    tags = soup.find_all('div', {'data-id': True})
    for tag in tags:
        a = tag.find('p', 'title').find('a')
        if not a:
            pass
        video = Video()
        video.site = 'Xvideos'
        video.title = a.text
        video.href = basepath + a.attrs['href']
        video.thumb = tag.find('img').attrs['data-src']
        cache.writeline(video)
    hub.run(cache)
    red.run(cache)

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
    with open(file_, 'wb') as f:
        f.write(content)
    
    if stat(file_).st_size > 52000000:
        return 'file size'
    
    return file_
