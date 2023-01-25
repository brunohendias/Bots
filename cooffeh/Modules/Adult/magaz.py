from Modules.cache import Cache
from Models.Image import Image
from Modules.Adult import erome
from Shared import tools

cache = Cache(Image, tools.cacheName('magaz'))
def getImage(index=1):
    return cache.readline(index)

def getImages(basepath, ul):
    for tag in ul.find_all('li'):
        info = tag.find('a', 'cardLink')
        if not info:
            pass
        obj = Image()
        obj.name = info.text.strip()
        obj.img = tag.find('img').attrs['data-src']
        obj.site = basepath
        obj.page = basepath + info.attrs['href']
        cache.writeline(obj)

def run():
    if not cache.exist():
        cache.delOld('magaz')
        erome.run()
        basepath = 'https://www.playboytv.com'
        soup = tools.getSoup(basepath)
        getImages(basepath, soup.find('ul', 'swiper-wrapper'))
        basepath = 'https://www.playboytv.com/models'
        soup = tools.getSoup(basepath)
        getImages(basepath, soup.find('ul', 'grid gridFive list-unstyled'))
