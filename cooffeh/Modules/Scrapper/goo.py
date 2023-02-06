from Models.Content import Content
from Modules.cache import Cache
from Shared import tools
from os import getenv
from json import loads
from random import randint

cache = Cache()
async def run(term:str,reqs:int=4):
    cache.clear()
    cx = getenv('GOOGLE_API_CX')
    key = getenv('GOOGLE_API_KEY')
    baseurl = 'https://customsearch.googleapis.com/customsearch/v1?cx='+cx
    start = 0
    for req in range(reqs):
        link = f'{baseurl}&key={key}&searchType=image&q={term}&start={start}'
        content = tools.get(link).content
        json = loads(content)
        for item in json['items']:
            obj = Content()
            obj.title = item['title']
            obj.img = item['link']
            obj.site = item['displayLink']
            obj.href = item['image']['contextLink']
            cache.add(obj)
        start += 20