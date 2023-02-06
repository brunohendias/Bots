from Modules.cache import Cache
from Models.Content import Content
from Shared import tools

cache = Cache()
async def openAlbum(album):
    href = album.find('a', 'album-link').attrs['href']
    soup = await tools.getSoup(href)
    title = soup.find('title').text
    for img in soup.find_all('img', 'img-front'):
        obj = Content()
        obj.site = 'erome.com'
        obj.title = title
        obj.img = img.attrs['data-src']
        obj.href = href
        cache.add(obj)
    for video in soup.find_all('video', { 'poster': True }):
        obj = Content()
        obj.site = 'erome.com'
        obj.title = title
        obj.img = video.attrs['poster']
        obj.link = video.find('source').attrs['src']
        cache.add(obj)

async def scrap(link:str):
    soup = await tools.getSoup(link)
    for album in soup.find_all('div', 'album'):
        await openAlbum(album)

async def run():
    cache.clear()
    await scrap('https://www.erome.com/explore/new')

async def search(term: str):
    cache.clear()
    await scrap(f'https://www.erome.com/search?q={term}')
