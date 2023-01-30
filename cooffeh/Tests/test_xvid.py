from Modules.Adult import xvid
from pytest import mark

@mark.asyncio
async def test_if_download_content():
	xvid.cache.delOld('xvid')
	await xvid.run()
	assert xvid.cache.exist()

@mark.asyncio
async def test_if_read_cache():
	video = await xvid.getVideo()
	assert video.title

@mark.asyncio
async def test_if_get_video_link():
	video = await xvid.getLink(1)
	assert video['title']

@mark.asyncio
async def test_if_search_videos():
	await xvid.search('big ass')
	video = await xvid.getVideo()
	assert video.title

def test_if_delete_old_cache():
	xvid.cache.delOld('xvid')
	assert not xvid.cache.exist()

