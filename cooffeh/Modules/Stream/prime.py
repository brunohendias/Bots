from Modules.cache import Cache
from Models.Video import Video
from Models.Categorie import Categorie
from Shared import tools

cache = Cache(Video, tools.cacheName('prime'))
async def getVideo(index=1):
	return await cache.readline(index)

async def getMovies():
	basepath = 'https://www.primevideo.com'
	soup = await tools.getSoup(
		basepath + '/storefront/ref=atv_br_Comedy_c_9zZ8D2_1_2?merchId=RentBuy')
	for collection in soup.find_all('div', 'tst-collection'):
		for li in collection.find_all('li'):
			video = Video()
			video.site = 'Primevideo'
			h2 = collection.find('h2')
			if h2:
				video.categorie = h2.text
			a = li.find('a')
			if a:
				video.title = a.attrs['aria-label']
				video.href = basepath + a.attrs['href']
			img = li.find('img')
			if img:
				video.thumb = img.attrs['src']
				await cache.writeline(video)

	hero = soup.find('ul', 'tst-superhero-item')
	for li in hero.find_all('li'):
		video = Video()
		video.site = 'Primevideo'
		a = li.find('a')
		if a:
			video.title = a.attrs['title']
			video.href = a.attrs['href']
		img = li.find('img')
		if img:
			video.thumb = img.attrs['src']
		video.categorie = 'carousel'
		await cache.writeline(video)

async def run():
	await getMovies()

def getCategories(soup, basepath):
	categories = []
	dropdown = soup.find('ul', 'pv-categories-dropdown')
	for li in dropdown.find_all('li'):
		a = li.find('a')
		if a:		
			categorie = Categorie()
			categorie.name = a.text
			categorie.href = basepath + a.attrs['href']
			categories.append(categorie)
	return categories
