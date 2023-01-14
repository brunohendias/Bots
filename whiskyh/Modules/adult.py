from Models.Video import Video
from Modules.cache import Cache
from datetime import date
from bs4 import BeautifulSoup as bs
from requests import get
from time import sleep
from threading import Thread

class Adult:
    basepath = 'https://www.xvideos.com'
    
    def __init__(self):
        self.cache = Cache(f"{date.today()}-adult.txt")

    def run(self, index):
        segundos = 0
        video = self.cache.readline(Video, index)
        if video.title:
            return video
        Thread(target=self.getVideos, name="writeCache").start()
        while not video.title or segundos < 15:
            sleep(1)
            video = self.cache.readline(Video)
            segundos += 1
        return video

    def getVideos(self):
        soup = bs(get(self.basepath).text, 'html.parser')
        videos = soup.find('div', 'mozaique')
        for d in videos.find_all('div', {'data-id': True}):
            a = d.find('p', 'title').find('a')
            if not a:
                pass
            v = Video()
            v.title = a.text
            v.href = self.basepath + a.attrs['href']
            v.thumb = d.find('img').attrs['data-src']
            self.cache.writeline(v)
        self.hub()

    def hub(self):
        self.basepath = 'https://pt.pornhub.com'
        soup = bs(get(self.basepath).text, 'html.parser')
        for d in soup.find_all('li', 'pcVideoListItem'):
            a = d.find('a')
            if not a:
                pass
            v = Video()
            v.title = a.attrs['title']
            v.href = self.basepath + a.attrs['href']
            v.thumb = a.find('img').attrs['src']
            self.cache.writeline(v)

    def getContentsTv(self, dados):
        for tag in dados:
            ctv = Content()
            try:
                info = tag.find('a', 'cardLink')
                ctv.name = info.text.strip()
                ctv.link = baseurl + info.attrs['href']
                ctv.img = tag.find('img').attrs['data-src']
                try:
                    ctv.topic = tag.find('div', 'tag').text.strip()
                except:
                    topic = tag.find('a')
                    ctv.topic = topic.text.strip()
                    ctv.linktopic = baseurl + topic.attrs['href']
                self.cache.writeline(ctv)
            except:
                pass

    def playboytv(self):
        self.basepath = 'https://www.playboytv.com'
        soup = bs(get(self.basepath).text, 'html.parser')
        self.getContentsTv(soup.find('ul', 'swiper-wrapper').find_all('li'))
        self.basepath = 'https://www.playboytv.com/models'
        soup = bs(get(self.basepath).text, 'html.parser')
        self.getContentsTv(soup.find('ul', 'grid gridFive list-unstyled').find_all('li'))

    def download(self, href):
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
        return file_
