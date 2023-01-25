from Modules.cache import Cache
from Models.Video import Video
from Shared import tools
from json import dumps, loads

basepath = 'https://www.brasileirinhas.com.br'
cache = Cache(Video, tools.cacheName('brasa'))
def getVideo(index=1):
	return cache.readline(index)

def run():
	if not cache.exist():
		cache.delOld('brasa')
		soup = tools.getSoup(basepath + '/home.html')
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
				cache.writeline(video)

def search(term:str):
	run()