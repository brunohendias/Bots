from Modules.Adult import hub

def test_if_download_content():
	hub.cache.delOld('hub')
	hub.run()
	assert hub.cache.exist()

def test_if_read_cache():
	video = hub.getVideo()
	assert video.title and video.site and video.thumb

def test_if_get_gif_link():
	resp = hub.getLink(1)
	assert resp and resp['link'] and resp['title']

def test_if_delete_old_cache():
	hub.cache.delOld('hub')
	assert not hub.cache.exist()
