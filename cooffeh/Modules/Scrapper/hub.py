from Modules.cache import Cache
from Models.Content import Content
from Shared import tools

basepath = 'https://pt.pornhub.com'
cache = Cache()
async def scrap(link:str):
    soup = await tools.getSoup(link)
    for tag in soup.find_all('li', 'pcVideoListItem'):
        a = tag.find('a')
        if a:
            obj = Content()
            obj.site = 'PornHub'
            obj.title = a.attrs['title']
            obj.href = basepath + a.attrs['href']
            obj.img = a.find('img').attrs['src']
            img = tag.find('img', {'data-mediabook': True})
            if img:
                obj.link = img.attrs['data-mediabook']
                cache.add(obj)

async def run():
    cache.clear()
    await scrap(basepath)

async def search(term:str):
    cache.clear()
    await scrap(basepath + f'/video/search?search={term}')
