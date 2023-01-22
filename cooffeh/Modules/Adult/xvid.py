from Modules.cache import Cache
from Models.Video import Video
from Shared import tools
from bs4 import BeautifulSoup as bs
from requests import get

basepath = 'https://www.xvideos.com'
cache = Cache(Video, tools.cacheName('xvid'))
def getVideo(index=1):
    return cache.readline(index)

def getData(soup):
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

def run():
    if not cache.exist():
        cache.delOld('xvid')
        html = get(basepath).text
        soup = bs(html, 'html.parser')
        getData(soup)
        for page in ['/new/1','/new/2']:
            html = get(basepath + page).text
            soup = bs(html, 'html.parser')
            getData(soup)

def getLink(index):
    video = getVideo(index)
    html = get(video.href).text
    soup = bs(html, 'html.parser')
    div = soup.find('div', {'id': 'html5video_base'})
    return {'link': div.find('a').attrs['href'], 'title': video.title}

def search(term: str):
    cache.delOld('xvid')
    query = f'/?k={term}'
    html = get(basepath + query).text
    soup = bs(html, 'html.parser')
    getData(soup)
    for page in ['&p=1','&p=2']:
        html = get(basepath + query + page).text
        soup = bs(html, 'html.parser')
        getData(soup)
