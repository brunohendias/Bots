from Modules import renderhtml
from Modules.cache import Cache
from Models.Video import Video
from Shared import tools

cache = Cache(Video, tools.cacheName('flix'))
async def getVideo(index=1):
	return await cache.readline(index)

async def getMedia():
	basepath = 'https://media.netflix.com/en'
	html = renderhtml.render(basepath)
	soup = tools.bs(html, 'html.parser')
	for media in soup.find_all('div', 'item-enter-done'):
		video = Video()
		video.site = 'NetFlix'
		video.title = media.find('h1').text
		video.href = media.find('a').attrs['href']
		await cache.writeline(video)

async def getNews():
	basepath = 'https://about.netflix.com/en'
	html = renderhtml.render(basepath + '/new-to-watch')
	soup = tools.bs(html, 'html.parser')
	sched = soup.find('div', {'id': 'release-schedule'})
	for div in sched.find_all('div', {'tabindex': True}):
		img = div.find('img')
		if img:
			a = div.find('a')
			video = Video()
			video.site = 'NetFlix'
			video.title = a.attrs['aria-label']
			video.href = a.attrs['href']
			video.thumb = img.attrs['src']
			await cache.writeline(video)

async def run():
	if not cache.exist():
		await getNews()