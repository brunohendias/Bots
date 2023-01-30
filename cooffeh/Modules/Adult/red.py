from Modules.cache import Cache
from Models.Video import Video
from Shared import tools
from json import loads

basepath = 'https://www.redtube.com'
cache = Cache(Video, tools.cacheName('red'))
async def getVideo(index=1):
    return await cache.readline(index)

async def getData(link:str):
    soup = await tools.getSoup(link)
    for li in soup.find_all('li'):
        div = li.find('div', 'video_title')
        if div:
            a = div.find('a')
            duration = li.find('span', 'duration')
            obj = Video()
            obj.site = 'RedTube'
            if duration:
                obj.title = a.text.strip() + duration.text.replace(' ', '').replace('\n', ' ')
            else:
                obj.title = a.text.strip()
            obj.href = basepath + a.attrs['href']
            img = li.find('img')
            obj.thumb = img.attrs['data-src']
            try:
                obj.link = img.attrs['data-mediabook']
            except:
                pass
            await cache.writeline(obj)

async def run():
    if not cache.exist():
        cache.delOld('red')
        await getData(basepath)
        for page in ['2', '3']:
            await getData(basepath + '/?page=' + page)

async def getLink(index:int):
    video = await getVideo(index)
    return {'link': video.link, 'title': video.title}

async def search(term:str):
    cache.delOld('red')
    await getData(basepath + f'/?search={term}')
    for page in ['2', '3']:
        await getData(basepath + f'/?search={term}&page=' + page)

async def getRealLink(index:int):
    video = await getVideo(index)
    soup = await tools.getSoup(video.href)
    script = soup.find('script', { 'id': 'tm_pc_player_setup'}).text
    values = script.replace('\\', '')
    for value in values.split(','):
        if 'media/mp4' in value:
            media = value.split('"')[3]
            json = tools.get(media).text
            qualitys = loads(json)
            return {'link': qualitys[0]['videoUrl'], 'title': video.title}
