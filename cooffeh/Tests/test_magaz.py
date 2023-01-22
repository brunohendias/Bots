from Modules.Adult import magaz

def test_if_download_content():
	magaz.cache.delOld('magaz')
	magaz.run()
	assert magaz.cache.exist()

def test_if_read_cache():
	image = magaz.getImage()
	assert image.name and image.site and image.img

def test_if_delete_old_cache():
	magaz.cache.delOld('magaz')
	assert not magaz.cache.exist()
