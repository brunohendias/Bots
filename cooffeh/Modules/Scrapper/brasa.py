from Modules.cache import Cache
from Models.Content import Content
from Shared import tools

basepath = 'https://www.brasileirinhas.com.br'
cache = Cache()
async def run():
	cache.clear()
	soup = await tools.getSoup(basepath + '/home.html')
	for carousel in soup.find_all('div', {'id': 'carousel-itens'}):
		for item in carousel.find_all('div', 'item'):
			img = item.find('img')
			obj = Content()
			obj.site = 'Brasileirinhas'
			obj.title = img.attrs['title']
			obj.href = basepath + item.find('a').attrs['href']
			try:
				obj.img = img.attrs['data-src']
			except:
				obj.img = img.attrs['src']
			cache.add(obj)

async def search(term:str):
	await run()