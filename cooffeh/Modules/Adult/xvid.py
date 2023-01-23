from Modules.cache import Cache
from Models.Video import Video
from Shared import tools
from bs4 import BeautifulSoup as bs
from requests import get

basepath = 'https://www.xvideos.com'
cache = Cache(Video, tools.cacheName('xvid'))
def getVideo(index=1):
    return cache.readline(index)

def getData(link:str):
    html = get(link).text
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

def run():
    if not cache.exist():
        cache.delOld('xvid')
        getData(basepath)
        for page in ['1','2']:
            getData(basepath + '/new/' +page)

def getLink(index:int):
    video = getVideo(index)
    html = get(video.href).text
    soup = bs(html, 'html.parser')
    div = soup.find('div', {'id': 'html5video_base'})
    return {'link': div.find('a').attrs['href'], 'title': video.title}

def search(term:str):
    cache.delOld('xvid')
    getData(basepath + f'/?k={term}')
    for page in ['1','2']:
        getData(basepath + f'/?k={term}&p=' + page)
