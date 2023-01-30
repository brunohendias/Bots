from Modules.cache import Cache
from Models.Video import Video
from Shared import tools
from pytest import mark

cache = Cache(Video)
def test_if_set_default_cache_path():
	assert cache.path == './Contents/cache.txt'

def test_if_set_cache_path():
	file_ = tools.cacheName('teste')
	cache = Cache(Video, file_)
	assert cache.path == './Contents/'+file_

def test_if_set_cache_obj():
	assert cache.obj == Video

@mark.asyncio
async def test_if_validate_exist_cache():
	video = Video()
	video.title = 'Test Cache'
	await cache.writeline(video)
	assert cache.exist()

@mark.asyncio
async def test_if_read_cache():
	video = await cache.readline()
	assert video.title == 'Test Cache'

def test_if_delete_cache():
	cache.delOld('cache')
	assert not cache.exist()