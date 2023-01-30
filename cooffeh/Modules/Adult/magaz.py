from Modules.cache import Cache
from Models.Image import Image
from Modules.Adult import erome
from Shared import tools
import asyncio

cache = Cache(Image, tools.cacheName('magaz'))
async def getImage(index=1):
    return await cache.readline(index)

async def getImages(basepath, ul):
    for tag in ul.find_all('li'):
        info = tag.find('a', 'cardLink')
        if info:
            obj = Image()
            obj.name = info.text.strip()
            obj.img = tag.find('img').attrs['data-src']
            obj.site = basepath
            obj.page = basepath + info.attrs['href']
            await cache.writeline(obj)

async def runAsync():
    if not cache.exist():
        cache.delOld('magaz')
        await erome.run()
        basepath = 'https://www.playboytv.com'
        soup = await tools.getSoup(basepath)
        await getImages(basepath, soup.find('ul', 'swiper-wrapper'))
        basepath = 'https://www.playboytv.com/models'
        soup = await tools.getSoup(basepath)
        await getImages(basepath, soup.find('ul', 'grid gridFive list-unstyled'))

def run():
    asyncio.run(runAsync())