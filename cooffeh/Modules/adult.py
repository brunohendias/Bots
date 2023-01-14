from Models.Video import Video
from Modules.cache import Cache
from Modules.Adult.red import RedAdult
from Modules.Adult.hub import Hub
from datetime import date
from bs4 import BeautifulSoup as bs
from requests import get
from os import stat

class Adult:
    basepath = 'https://www.xvideos.com'
    
    def __init__(self):
        self.cache = Cache(Video, f"{date.today()}adult.txt")

    def getVideo(self, index):
        if self.cache.exist():
            return self.cache.readline(index)
        return Video()

    def run(self):
        html = get(self.basepath).text
        soup = bs(html, 'html.parser')
        videos = soup.find('div', 'mozaique')
        for d in videos.find_all('div', {'data-id': True}):
            a = d.find('p', 'title').find('a')
            if not a:
                pass
            v = Video()
            v.site = 'Xvideos'
            v.title = a.text
            v.href = self.basepath + a.attrs['href']
            v.thumb = d.find('img').attrs['data-src']
            self.cache.writeline(v)
        self.hub()
        self.red()

    def hub(self):
        return Hub(self.cache).run()
    
    def red(self):
        return RedAdult(self.cache).run()

    def download(self, href, link=''):
        if not link:
            div = bs(get(href).text, 'html.parser').find('div', {
                'id': 'html5video_base'
            })
            if not div:
                return 'no link'
            link = div.find('a').attrs['href']
        if 'http://' not in link and 'https://' not in link:
            return ''
        file_ = './Contents/video.mp4'
        with open(file_, 'wb') as f:
            f.write(get(link).content)
        if stat(file_).st_size > 52000000:
            return 'file size'
        return file_

def getVideo(index):
    return Adult().getVideo(index)

def run():
    return Adult().run()

def download(href, link):
    return Adult().download(href, link)