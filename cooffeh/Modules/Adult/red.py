from Models.Video import Video
from bs4 import BeautifulSoup as bs
from requests import get

basepath = 'https://www.redtube.com'

def getData(cache, ul):
    for tag in ul.find_all('li'):
        div = tag.find('div', 'video_title')
        if div:
            a = div.find('a')
            duration = tag.find('span', 'duration')
            video = Video()
            video.site = 'RedTube'
            if duration:
                video.title = a.text.strip() + duration.text.replace(' ', '').replace('\n', ' ')
            else:
                video.title = a.text.strip()
            video.href = basepath + a.attrs['href']
            img = tag.find('img')
            video.thumb = img.attrs['data-src']
            video.link = img.attrs['data-mediabook']
            cache.writeline(video)

def run(cache):
    html = get(basepath).text
    if not html:
        return ''
    soup = bs(html, 'html.parser')
    ul = soup.find('ul', { 'id': 'block_hottest_videos_by_country' })
    getData(cache, ul)
    ul = soup.find('ul', { 'id': 'block_recommended_videos' })
    getData(cache, ul)
    ul = soup.find('ul', { 'id': 'most_recent_videos' })
    getData(cache, ul)
    ul = soup.find('ul', { 'id': 'recommended_videos_menu_block' })
    getData(cache, ul)
    ul = soup.find('ul', { 'id': 'trending_videos_block' })
    getData(cache, ul)
