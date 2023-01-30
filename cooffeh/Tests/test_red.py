from Modules.Adult import red
from pytest import mark

@mark.asyncio
async def test_if_download_content():
	red.cache.delOld('red')
	await red.run()
	assert red.cache.exist()

@mark.asyncio
async def test_if_read_cache():
	video = await red.getVideo()
	assert video.title

@mark.asyncio
async def test_if_get_gif_link():
	video = await red.getLink(1)
	assert video['title']

@mark.asyncio
async def test_if_get_video_link():
	video = await red.getRealLink(1)
	assert video['title']

def test_if_delete_old_cache():
	red.cache.delOld('red')
	assert not red.cache.exist()

