from Modules.cache import Cache
from Models.Video import Video
from Shared import tools
from json import dumps, loads

basepath = 'https://www.brasileirinhas.com.br'
cache = Cache(Video, tools.cacheName('brasa'))
async def getVideo(index=1):
	return await cache.readline(index)

async def run():
	if not cache.exist():
		cache.delOld('brasa')
		soup = await tools.getSoup(basepath + '/home.html')
		for carousel in soup.find_all('div', {'id': 'carousel-itens'}):
			for item in carousel.find_all('div', 'item'):
				video = Video()
				video.site = 'Brasileirinhas'
				img = item.find('img')
				video.title = img.attrs['title']
				video.href = basepath + item.find('a').attrs['href']
				try:
					video.thumb = img.attrs['data-src']
				except:
					video.thumb = img.attrs['src']
				await cache.writeline(video)

async def search(term:str):
	await run()