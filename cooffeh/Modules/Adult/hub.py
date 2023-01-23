from Modules.cache import Cache
from Models.Video import Video
from Shared import tools
from bs4 import BeautifulSoup as bs
from requests import get

basepath = 'https://pt.pornhub.com'
cache = Cache(Video, tools.cacheName('hub'))
def getVideo(index=1):
    return cache.readline(index)

def getData(link:str):
    html = get(link).text
    soup = bs(html, 'html.parser')
    tags = soup.find_all('li', 'pcVideoListItem')
    for tag in tags:
        a = tag.find('a')
        if a:
            obj = Video()
            obj.site = 'PornHub'
            obj.title = a.attrs['title']
            obj.href = basepath + a.attrs['href']
            obj.thumb = a.find('img').attrs['src']
            img = tag.find('img')
            try:
                obj.link = img.attrs['data-mediabook']
            except:
                pass
            cache.writeline(obj)

def run():
    if not cache.exist():
        cache.delOld('hub')
        getData(basepath)
        for page in ['2', '3']:
            getData(basepath + '/video?page=' + page)

def getLink(index:int):
    video = getVideo(index)
    return {'link': video.link, 'title': video.title}

def search(term:str):
    cache.delOld('hub')
    getData(basepath + f'/video/search?search={term}')
    for page in ['2', '3']:
        getData(basepath + f'/video/search?search={term}&page=' + page)
