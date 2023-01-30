from Modules.cache import Cache
from Models.Video import Video
from Shared import tools

basepath = 'https://pt.pornhub.com'
cache = Cache(Video, tools.cacheName('hub'))
async def getVideo(index=1):
    return await cache.readline(index)

async def getData(link:str):
    soup = await tools.getSoup(link)
    for tag in soup.find_all('li', 'pcVideoListItem'):
        a = tag.find('a')
        if a:
            obj = Video()
            obj.site = 'PornHub'
            obj.title = a.attrs['title']
            obj.href = basepath + a.attrs['href']
            obj.thumb = a.find('img').attrs['src']
            img = tag.find('img', {'data-mediabook': True})
            if img:
                obj.link = img.attrs['data-mediabook']
                await cache.writeline(obj)

async def run():
    if not cache.exist():
        cache.delOld('hub')
        await getData(basepath)
        for page in ['2', '3']:
            await getData(basepath + '/video?page=' + page)

async def getLink(index:int):
    video = await getVideo(index)
    return {'link': video.link, 'title': video.title}

async def search(term:str):
    cache.delOld('hub')
    await getData(basepath + f'/video/search?search={term}')
    for page in ['2', '3']:
        await getData(basepath + f'/video/search?search={term}&page=' + page)
