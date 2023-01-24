from Modules.cache import Cache
from Models.Video import Video
from Shared import tools

cache = Cache(Video)
def test_if_set_default_cache_path():
	assert cache.path == './Contents/cache.txt'

def test_if_set_cache_path():
	file_ = tools.cacheName('teste')
	cache = Cache(Video, file_)
	assert cache.path == './Contents/'+file_

def test_if_set_cache_obj():
	assert cache.obj == Video

def test_if_validate_exist_cache():
	video = Video()
	video.title = 'Test Cache'
	cache.writeline(video)
	assert cache.exist()

def test_if_read_cache():
	assert cache.readline().title == 'Test Cache'

def test_if_delete_cache():
	cache.delOld('cache')
	assert not cache.exist()