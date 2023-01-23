from Modules.cache import Cache
from Models.Video import Video
from Shared import tools
from bs4 import BeautifulSoup as bs
from requests import get
from json import loads

basepath = 'https://www.redtube.com'
cache = Cache(Video, tools.cacheName('red'))
def getVideo(index=1):
    return cache.readline(index)

def getData(link:str):
    html = get(link).text
    soup = bs(html, 'html.parser')
    for li in soup.find_all('li'):
        div = li.find('div', 'video_title')
        if div:
            a = div.find('a')
            duration = li.find('span', 'duration')
            obj = Video()
            obj.site = 'RedTube'
            if duration:
                obj.title = a.text.strip() + duration.text.replace(' ', '').replace('\n', ' ')
            else:
                obj.title = a.text.strip()
            obj.href = basepath + a.attrs['href']
            img = li.find('img')
            obj.thumb = img.attrs['data-src']
            try:
                obj.link = img.attrs['data-mediabook']
            except:
                pass
            cache.writeline(obj)

def run():
    if not cache.exist():
        cache.delOld('red')
        getData(basepath)
        for page in ['2', '3']:
            getData(basepath + '/?page=' + page)

def getLink(index:int):
    video = getVideo(index)
    return {'link': video.link, 'title': video.title}

def search(term:str):
    cache.delOld('red')
    getData(basepath + f'/?search={term}')
    for page in ['2', '3']:
        getData(basepath + f'/?search={term}&page=' + page)

def getRealLink(index:int):
    video = getVideo(index)
    html = get(video.href).text
    soup = bs(html, 'html.parser')
    script = soup.find('script', { 'id': 'tm_pc_player_setup'}).text
    values = script.replace('\\', '')
    for value in values.split(','):
        if 'media/mp4' in value:
            media = value.split('"')[3]
            json = get(media).text
            qualitys = loads(json)
            return {'link': qualitys[0]['videoUrl'], 'title': video.title}
