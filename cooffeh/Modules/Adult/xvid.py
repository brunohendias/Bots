from Modules.cache import Cache
from Models.Video import Video
from Shared import tools
from bs4 import BeautifulSoup as bs
from requests import get

cache = Cache(Video, tools.cacheName('xvid'))
adultCache = Cache(Video, tools.cacheName('adult'))
def getVideo(index=1):
    return cache.readline(index)

def run():
    if not cache.exist():
        cache.delOld('xvid')
        basepath = 'https://www.xvideos.com'
        html = get(basepath).text
        soup = bs(html, 'html.parser')
        tags = soup.find_all('div', {'data-id': True})
        for tag in tags:
            a = tag.find('p', 'title').find('a')
            if not a:
                pass
            obj = Video()
            obj.site = 'Xvideos'
            obj.title = a.text
            obj.href = basepath + a.attrs['href']
            obj.thumb = tag.find('img').attrs['data-src']
            cache.writeline(obj)
            adultCache.writeline(obj)
