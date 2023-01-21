from Modules.cache import Cache
from Models.Video import Video
from Shared import tools
from bs4 import BeautifulSoup as bs
from requests import get

cache = Cache(Video, tools.cacheName('hub'))
def getVideo(index=1):
    return cache.readline(index)

def run():
    if not cache.exist():
        cache.delOld('hub')
        basepath = 'https://pt.pornhub.com'
        html = get(basepath).text
        if not html:
            return ''
        soup = bs(html, 'html.parser')
        tags = soup.find_all('li', 'pcVideoListItem')
        for tag in tags:
            a = tag.find('a')
            if not a:
                pass
            obj = Video()
            obj.site = 'PornHub'
            obj.title = a.attrs['title']
            obj.href = basepath + a.attrs['href']
            obj.thumb = a.find('img').attrs['src']
            cache.writeline(obj)
