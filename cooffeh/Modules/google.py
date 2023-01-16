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
    start = 0
    cx = getenv('GOOGLE_API_CX')
    key = '&key=' + getenv('GOOGLE_API_KEY')
    baseurl = 'https://customsearch.googleapis.com/customsearch/v1?cx='+cx
    query = '&q=' + term.replace(" ", "+")

    for r in range(5):
        start = f'&start={start}'
        link = ''.join([baseurl, key, '&searchType=image', query, start])
        content = get(link).content
        json = loads(content)

        for item in json['items']:
            image = Image()
            image.name = item['title']
            image.img = item['link']
            image.site = item['displayLink']
            image.page = item['image']['contextLink']
            image.searchTerms = term
            cache.writeline(image)
        start = randint(10, 100)
