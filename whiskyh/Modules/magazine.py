from Modules.cache import Cache
from datetime import date
from bs4 import BeautifulSoup as bs
from requests import get
from time import sleep
from threading import Thread

class Content:
    name = ''
    img = ''
    link = ''

    def __repr__(self):
        return self.name

class Magazine:
    basepath = 'https://www.playboytv.com'
    error = False
    
    def __init__(self):
        self.cache = Cache(f"{date.today()}-magazine.txt")

    def run(self, index):
        segundos = 0
        content = self.cache.readline(Content, index)
        if content.name:
            return content
        Thread(target=self.getHTML, name="writeCache").start()
        while not content.name or segundos < 15:
            sleep(1)
            content = self.cache.readline(Content)
            segundos += 1
        return content

    def getHTML(self):
        soup = bs(get(self.basepath).text, 'html.parser')
        self.getImages(soup.find('ul', 'swiper-wrapper').find_all('li'))
        self.basepath = 'https://www.playboytv.com/models'
        soup = bs(get(self.basepath).text, 'html.parser')
        self.getImages(soup.find('ul', 'grid gridFive list-unstyled').find_all('li'))

    def getImages(self, dados):
        for tag in dados:
            ctv = Content()
            try:
                info = tag.find('a', 'cardLink')
                ctv.name = info.text.strip()
                ctv.img = tag.find('img').attrs['data-src']
                ctv.link = self.basepath + info.attrs['href']
                self.cache.writeline(ctv)
            except:
                pass