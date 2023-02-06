from Modules.cache import Cache
from Models.Content import Content
from Shared import tools

basepath = 'https://www.xvideos.com'
cache = Cache()
async def getLink(href:str):
    if not href:
        return ''
    soup = await tools.getSoup(href)
    div = soup.find('div', {'id': 'html5video_base'})
    return div.find('a').attrs['href'] if div else ''

async def scrap(link:str):
    soup = await tools.getSoup(link)
    for tag in soup.find_all('div', {'data-id': True}):
        a = tag.find('p', 'title').find('a')
        if a:
            obj = Content()
            obj.site = 'Xvideos'
            obj.title = a.text
            obj.img = tag.find('img').attrs['data-src']
            obj.link = await getLink(basepath + a.attrs['href'])
            if obj.link:
                cache.add(obj)

async def run():
    cache.clear()
    return await scrap(basepath)

async def search(term:str):
    cache.clear()
    return await scrap(basepath + f'/?k={term}')
