from Modules.cache import Cache
from Models.Video import Video
from Shared import tools

basepath = 'https://www.xvideos.com'
cache = Cache(Video, tools.cacheName('xvid'))
async def getVideo(index:int=1):
    return await cache.readline(index)

async def scrap(link:str):
    soup = await tools.getSoup(link)
    for tag in soup.find_all('div', {'data-id': True}):
        a = tag.find('p', 'title').find('a')
        if a:
            obj = Video()
            obj.site = 'Xvideos'
            obj.title = a.text
            obj.href = basepath + a.attrs['href']
            obj.thumb = tag.find('img').attrs['data-src']
            await cache.writeline(obj)

async def run():
    if not cache.exist():
        cache.delOld('xvid')
        await scrap(basepath)
        for page in ['1','2']:
            await scrap(basepath + '/new/' +page)

async def getLink(index:int):
    video = await getVideo(index)
    soup = await tools.getSoup(video.href)
    div = soup.find('div', {'id': 'html5video_base'})
    return {'link': div.find('a').attrs['href'], 'title': video.title}

async def search(term:str):
    cache.delOld('xvid')
    await scrap(basepath + f'/?k={term}')
    for page in ['1','2']:
        await scrap(basepath + f'/?k={term}&p=' + page)
