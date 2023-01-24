from Modules.Adult import hub

def test_if_download_content():
	hub.cache.delOld('hub')
	hub.run()
	assert hub.cache.exist()

def test_if_read_cache():
	assert hub.getVideo().title

def test_if_get_gif_link():
	assert hub.getLink(1)['title']

def test_if_delete_old_cache():
	hub.cache.delOld('hub')
	assert not hub.cache.exist()
