from Models.Image import Image
from Modules.cache import Cache
from Shared import tools
from os import getenv
from requests import get
from json import loads
from random import randint
cache = Cache(Image, tools.cacheName('google'))

def getImage(index):
    return cache.readline(index)

def searchImages(term:str, total=40):
    cache.delOld('google')
    cx = getenv('GOOGLE_API_CX')
    key = '&key=' + getenv('GOOGLE_API_KEY')
    baseurl = 'https://customsearch.googleapis.com/customsearch/v1?cx='+cx
    query = '&q=' + term.replace(" ", "+")
    ini, end, salto, limite = 0, 0, 20, 80
    totreq = limite // salto
    for r in range(totreq):
        ini = end
        end += salto
        start = f'&start={randint(ini, end)}'
        link = ''.join([baseurl, key, '&searchType=image', query, start])
        content = get(link).content
        json = loads(content)
        for item in json['items']:
            obj = Image()
            obj.name = item['title']
            obj.img = item['link']
            obj.site = item['displayLink']
            obj.page = item['image']['contextLink']
            obj.searchTerms = term
            cache.writeline(obj)
