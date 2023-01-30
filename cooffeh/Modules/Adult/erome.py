from Modules.cache import Cache
from Models.Image import Image
from Shared import tools

cache = Cache(Image, tools.cacheName('magaz'))
async def getImages(link:str):
    soup = await tools.getSoup(link)
    albums = soup.find('div', 'page-content row')
    if albums:
        for album in albums.find_all('div', 'album'):
            obj = Image()
            obj.site = 'erome.com'
            obj.name = album.find('span', 'album-title').text
            obj.page = album.find('a').attrs['href']
            img = album.find('img', {'data-rotate-src': True})
            if img:
                obj.img = img.attrs['data-rotate-src']
                await cache.writeline(obj)

async def run():
    basepath = 'https://www.erome.com/explore/new'
    for page in range(5):
        await getImages(basepath + f'?page={page+1}')
