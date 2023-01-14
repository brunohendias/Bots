from Modules.cache import Cache
from datetime import date
from bs4 import BeautifulSoup as bs
from requests import get

class Content:
    name = ''
    img = ''
    link = ''

class Magazine:
    basepath = 'https://www.playboytv.com'
    
    def __init__(self):
        self.cache = Cache(Content, f"{date.today()}magaz.txt")

    def getImage(self, index):
        if self.cache.exist():
            return self.cache.readline(index)
        return Content()

    def run(self):
        html = get(self.basepath).text
        soup = bs(html, 'html.parser')
        self.getImages(soup.find('ul', 'swiper-wrapper').find_all('li'))
        self.basepath = 'https://www.playboytv.com/models'
        html = get(self.basepath).text
        soup = bs(html, 'html.parser')
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

def run():
    return Magazine().run()

def getImage(index):
    return Magazine().getImage(index)
