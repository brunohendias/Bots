from Modules.cache import Cache
from Models.Image import Image
from Shared import tools

cache = Cache(Image, tools.cacheName('play'))
async def getImage(index:int=1):
    return await cache.readline(index)

async def scrap(link:str):
    soup = await tools.getSoup(link)
    for li in soup.find_all('li'):
        info = li.find('a', 'cardLink')
        if info:
            obj = Image()
            obj.name = info.text.strip()
            obj.img = li.find('img').attrs['data-src']
            obj.site = 'playboytv.com/models'
            obj.page = link + info.attrs['href']
            await cache.writeline(obj)

async def run():
    if not cache.exist():
        cache.delOld('play')
        await scrap('https://www.playboytv.com/models')
