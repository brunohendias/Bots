from Modules.Adult import xvid

def test_if_download_content():
	xvid.cache.delOld('xvid')
	xvid.run()
	assert xvid.cache.exist()

def test_if_read_cache():
	assert xvid.getVideo().title

def test_if_get_video_link():
	assert xvid.getLink(1)['title']

def test_if_search_videos():
	xvid.search('big ass')
	assert xvid.getVideo().title

def test_if_delete_old_cache():
	xvid.cache.delOld('xvid')
	assert not xvid.cache.exist()

