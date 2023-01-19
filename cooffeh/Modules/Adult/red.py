from Modules.cache import Cache
from Models.Video import Video
from Shared import tools
from bs4 import BeautifulSoup as bs
from requests import get

basepath = 'https://www.redtube.com'
cache = Cache(Video, tools.cacheName('red'))
adultCache = Cache(Video, tools.cacheName('adult'))
def getVideo(index=1):
    return cache.readline(index)

def getData(ul):
    for tag in ul.find_all('li'):
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
            adultCache.writeline(obj)

def run():
    if not cache.exist():
        cache.delOld('xvid')
        html = get(basepath).text
        if not html:
            return ''
        soup = bs(html, 'html.parser')
        getData(soup.find('ul', {'id': 'block_hottest_videos_by_country'}))
        getData(soup.find('ul', {'id': 'block_recommended_videos'}))
        getData(soup.find('ul', {'id': 'most_recent_videos'}))
        getData(soup.find('ul', {'id': 'recommended_videos_menu_block'}))
        getData(soup.find('ul', {'id': 'trending_videos_block'}))
