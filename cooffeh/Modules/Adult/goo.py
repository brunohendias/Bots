from Models.Image import Image
from Modules.cache import Cache
from Shared import tools
from os import getenv
from json import loads
from random import randint

cache = Cache(Image, tools.cacheName('google'))
async def getImage(index=1):
    return await cache.readline(index)

async def run(term:str,reqs=4):
    cache.delOld('google')
    cx = getenv('GOOGLE_API_CX')
    key = getenv('GOOGLE_API_KEY')
    baseurl = 'https://customsearch.googleapis.com/customsearch/v1?cx='+cx
    start = 0
    for req in range(reqs):
        link = f'{baseurl}&key={key}&searchType=image&q={term}&start={start}'
        content = tools.get(link).content
        json = loads(content)
        for item in json['items']:
            obj = Image()
            obj.name = item['title']
            obj.img = item['link']
            obj.site = item['displayLink']
            obj.page = item['image']['contextLink']
            obj.searchTerms = term
            await cache.writeline(obj)
        start += 20