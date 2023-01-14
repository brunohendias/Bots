from Models.Video import Video
from Modules.cache import Cache
from datetime import date
from bs4 import BeautifulSoup as bs
from requests import get

class Hub:
    basepath = 'https://pt.pornhub.com'

    def __init__(self, cache):
        self.cache = cache

    def run(self):
        html = get(self.basepath).text
        soup = bs(html, 'html.parser')
        for d in soup.find_all('li', 'pcVideoListItem'):
            a = d.find('a')
            if not a:
                pass
            v = Video()
            v.site = 'PornHub'
            v.title = a.attrs['title']
            v.href = self.basepath + a.attrs['href']
            v.thumb = a.find('img').attrs['src']
            self.cache.writeline(v)
