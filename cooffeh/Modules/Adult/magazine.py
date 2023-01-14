from Modules.cache import Cache
from Models.Image import Image
from Shared import tools
from bs4 import BeautifulSoup as bs
from requests import get

cache = Cache(Image, tools.cacheName('magaz'))
def getImage(index=1):
    return cache.readline(index)

def getImages(basepath, ul):
    for tag in ul.find_all('li'):
        info = tag.find('a', 'cardLink')
        if not info:
            pass
        image = Image()
        image.name = info.text.strip()
        image.img = tag.find('img').attrs['data-src']
        image.link = basepath + info.attrs['href']
        cache.writeline(image)

def run():
    if cache.exist():
        return True
    cache.delOld()
    basepath = 'https://www.playboytv.com'
    html = get(basepath).text
    soup = bs(html, 'html.parser')
    getImages(basepath, soup.find('ul', 'swiper-wrapper'))
    basepath = 'https://www.playboytv.com/models'
    html = get(basepath).text
    soup = bs(html, 'html.parser')
    getImages(basepath, soup.find('ul', 'grid gridFive list-unstyled'))
