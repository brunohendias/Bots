from Modules.cache import Cache
from Models.Content import Content
from Shared import tools
from json import loads

basepath = 'https://www.redtube.com'
cache = Cache()
async def getLink(href:str):
    if not href:
        return ''
    soup = await tools.getSoup(href)
    script = soup.find('script', { 'id': 'tm_pc_player_setup'})
    if script:
        values = script.text.replace('\\', '')
        for value in values.split(','):
            if 'media/mp4' in value:
                media = value.split('"')[3]
                json = tools.get(media).text
                qualitys = loads(json)
                return qualitys[0]['videoUrl']

async def scrap(link:str):
    soup = await tools.getSoup(link)
    for li in soup.find_all('li'):
        div = li.find('div', 'video_title')
        if div:
            a = div.find('a')
            duration = li.find('span', 'duration')
            obj = Content()
            obj.site = 'RedTube'
            obj.title = a.text.strip() + (duration.text.replace(
                ' ', '').replace('\n', ' ') if duration else '')
            obj.img = li.find('img', { 'data-src': True}).attrs['data-src']
            obj.link = await getLink(basepath + a.attrs['href'])
            cache.add(obj)

async def run():
    cache.clear()
    await scrap(basepath)

async def search(term:str):
    cache.clear()
    await scrap(basepath + f'/?search={term}')
