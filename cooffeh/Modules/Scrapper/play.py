from Modules.cache import Cache
from Models.Content import Content
from Shared import tools

cache = Cache()
async def scrap(link:str):
    soup = await tools.getSoup(link)
    for li in soup.find_all('li'):
        info = li.find('a', 'cardLink')
        if info:
            obj = Content()
            obj.title = info.text.strip()
            obj.img = li.find('img').attrs['data-src']
            obj.site = 'playboytv.com/models'
            obj.href = link + info.attrs['href']
            cache.add(obj)

async def run():
    cache.clear()
    await scrap('https://www.playboytv.com/models')
