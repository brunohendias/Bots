from Modules.cache import Cache
from Models.Content import Content
from Shared import tools

cache = Cache()
async def scrap():
	basepath = 'https://www.primevideo.com'
	soup = await tools.getSoup(
		basepath + '/storefront/ref=atv_br_Comedy_c_9zZ8D2_1_2?merchId=RentBuy')
	for collection in soup.find_all('div', 'tst-collection'):
		for li in collection.find_all('li'):
			obj = Content()
			obj.site = 'Primevideo'
			h2 = collection.find('h2')
			if h2:
				obj.categorie = h2.text
			a = li.find('a')
			if a:
				obj.title = a.attrs['aria-label']
				obj.href = basepath + a.attrs['href']
			img = li.find('img')
			if img:
				obj.thumb = img.attrs['src']
				cache.add(video)

	hero = soup.find('ul', 'tst-superhero-item')
	for li in hero.find_all('li'):
		obj = Content()
		obj.site = 'Primevideo'
		a = li.find('a')
		if a:
			obj.title = a.attrs['title']
			obj.href = a.attrs['href']
		img = li.find('img')
		if img:
			obj.thumb = img.attrs['src']
		obj.categorie = 'carousel'
		cache.add(video)

async def run():
	cache.clear()
	await scrap()
