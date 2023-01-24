from Modules.Adult import red

def test_if_download_content():
	red.cache.delOld('red')
	red.run()
	assert red.cache.exist()

def test_if_read_cache():
	assert red.getVideo().title

def test_if_get_gif_link():
	assert red.getLink(1)['title']

def test_if_get_video_link():
	assert red.getRealLink(1)['title']

def test_if_delete_old_cache():
	red.cache.delOld('red')
	assert not red.cache.exist()

