from Modules.cache import Cache
from Models.Image import Image
from Shared import tools

cache = Cache(Image, tools.cacheName('erome'))
async def getImage(index:int=1):
    return await cache.readline(index)

async def openAlbum(album):
    href = album.find('a', 'album-link').attrs['href']
    soup = await tools.getSoup(href)
    name = soup.find('title').text
    for img in soup.find_all('img', 'img-front'):
        obj = Image()
        obj.site = 'erome.com'
        obj.name = name
        obj.img = img.attrs['data-src']
        await cache.writeline(obj)
    for video in soup.find_all('video', { 'poster': True }):
        obj = Image()
        obj.site = 'erome.com'
        obj.name = name
        obj.img = video.attrs['poster']
        obj.page = video.find('source').attrs['src']
        await cache.writeline(obj)

async def scrap(link:str):
    soup = await tools.getSoup(link)
    for album in soup.find_all('div', 'album'):
        await openAlbum(album)

async def run():
    if not cache.exist():
        cache.delOld('erome')
        await scrap('https://www.erome.com/explore/new')

async def search(term: str):
    cache.delOld('erome')
    await scrap(f'https://www.erome.com/search?q={term}')
