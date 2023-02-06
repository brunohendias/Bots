from Modules import renderhtml
from Modules.cache import Cache
from Models.Content import Content
from Shared import tools

cache = Cache()
async def scrap():
	basepath = 'https://about.netflix.com/en'
	html = renderhtml.render(basepath + '/new-to-watch')
	soup = tools.bs(html, 'html.parser')
	sched = soup.find('div', {'id': 'release-schedule'})
	for div in sched.find_all('div', {'tabindex': True}):
		img = div.find('img')
		if img:
			a = div.find('a')
			obj = Content()
			obj.site = 'NetFlix'
			obj.title = a.attrs['aria-label']
			obj.href = a.attrs['href']
			obj.img = img.attrs['src']
			cache.add(obj)

async def run():
	cache.clear()
	await scrap()