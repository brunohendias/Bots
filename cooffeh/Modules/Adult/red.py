from Modules.cache import Cache
from Models.Video import Video
from Shared import tools
from bs4 import BeautifulSoup as bs
from requests import get
# from json import loads

cache = Cache(Video, tools.cacheName('red'))
def getVideo(index=1):
    return cache.readline(index)

def run():
    if not cache.exist():
        cache.delOld('red')
        basepath = 'https://www.redtube.com'
        html = get(basepath).text
        soup = bs(html, 'html.parser')
        for tag in soup.find_all('li'):
            div = tag.find('div', 'video_title')
            if div:
                a = div.find('a')
                duration = tag.find('span', 'duration')
                obj = Video()
                obj.site = 'RedTube'
                if duration:
                    obj.title = a.text.strip() + duration.text.replace(' ', '').replace('\n', ' ')
                else:
                    obj.title = a.text.strip()
                obj.href = basepath + a.attrs['href']
                img = tag.find('img')
                obj.thumb = img.attrs['data-src']
                obj.link = img.attrs['data-mediabook']
                cache.writeline(obj)

def getLink(index):
    video = getVideo(index)
    return {'link': video.link, 'title': video.title}
    # html = get(video.href).text
    # soup = bs(html, 'html.parser')
    # script = soup.find('script', { 'id': 'tm_pc_player_setup'}).text
    # values = script.replace('\\', '')
    # for value in values.split(','):
    #     if 'media/mp4' in value:
    #         media = value.split('"')[3]
    #         json = get(media).text
    #         qualitys = loads(json)
    #         return {'link': qualitys[0]['videoUrl'], 'title': video.title}
