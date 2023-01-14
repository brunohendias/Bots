from Models.Video import Video
from datetime import date
from bs4 import BeautifulSoup as bs
from requests import get

class RedAdult:
    basepath = 'https://www.redtube.com'

    def __init__(self, cache):
        self.cache = cache

    def getData(self, soup, id_):
        data = soup.find('ul', { 'id': id_ })
        if not data or data == None:
            return True
        for video in data.find_all('li'):
            divTitle = video.find('div', 'video_title')
            if divTitle:
                a = divTitle.find('a')
                duration = video.find('span', 'duration')
                v = Video()
                v.site = 'RedTube'
                if not duration or duration == None:
                    v.title = a.text.strip()
                else:
                    v.title = a.text.strip() + duration.text.replace(' ', '').replace('\n', ' ')
                v.href = self.basepath + a.attrs['href']
                img = video.find('img')
                v.thumb = img.attrs['data-src']
                v.link = img.attrs['data-mediabook']
                self.cache.writeline(v)

    def run(self):
        html = get(self.basepath).text
        soup = bs(html, 'html.parser')
        self.getData(soup, 'block_hottest_videos_by_country')
        self.getData(soup, 'block_recommended_videos')
        self.getData(soup, 'most_recent_videos')
        self.getData(soup, 'recommended_videos_menu_block')
        self.getData(soup, 'trending_videos_block')
