from Modules.Adult import hub
from pytest import mark

@mark.asyncio
async def test_if_download_content():
	hub.cache.delOld('hub')
	await hub.run()
	assert hub.cache.exist()

@mark.asyncio
async def test_if_read_cache():
	video = await hub.getVideo()
	assert video.title

@mark.asyncio
async def test_if_get_gif_link():
	video = await hub.getLink(1)
	assert video['title']

def test_if_delete_old_cache():
	hub.cache.delOld('hub')
	assert not hub.cache.exist()
