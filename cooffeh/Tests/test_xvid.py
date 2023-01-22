from Modules.Adult import xvid

def test_if_download_content():
	xvid.cache.delOld('xvid')
	xvid.run()
	assert xvid.cache.exist()

def test_if_read_cache():
	video = xvid.getVideo()
	assert video.title and video.site and video.thumb

def test_if_get_video_link():
	resp = xvid.getLink(1)
	assert resp and resp['link'] and resp['title']

def test_if_search_videos():
	xvid.search('big ass')
	video = xvid.getVideo()
	assert xvid.cache.exist() and video.title and video.site

def test_if_delete_old_cache():
	xvid.cache.delOld('xvid')
	assert not xvid.cache.exist()

