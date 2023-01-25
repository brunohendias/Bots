from json import loads, dumps
from Modules.cache import Cache
from Models.Image import Image
from Shared import tools

cache = Cache(Image, tools.cacheName('magaz'))
def getImages(soup):
    albums = soup.find('div', 'page-content row')
    for album in albums.find_all('div', 'album'):
        obj = Image()
        obj.name = album.find('span', 'album-title').text
        obj.page = album.find('a').attrs['href']
        obj.site = 'erome.com'
        for img in album.find_all('img'):
            try:
                obj.img = img.attrs['data-rotate-src']
                cache.writeline(obj)
            except:
                pass

def run():
    basepath = 'https://www.erome.com/explore/new'
    for page in range(5):
        next_ = f'?page={page+1}'
        getImages(tools.getSoup(basepath + next_))
