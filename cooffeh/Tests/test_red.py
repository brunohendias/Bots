from Modules.Adult import red

def test_if_download_content():
	red.cache.delOld('red')
	red.run()
	assert red.cache.exist()

def test_if_read_cache():
	video = red.getVideo()
	assert video.title and video.site and video.thumb

def test_if_get_gif_link():
	resp = red.getLink(1)
	assert resp and resp['link'] and resp['title']

def test_if_get_video_link():
	resp = red.getRealLink(1)
	assert resp and resp['link'] and resp['title']

def test_if_delete_old_cache():
	red.cache.delOld('red')
	assert not red.cache.exist()

