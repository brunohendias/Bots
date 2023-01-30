from Modules.Adult import magaz
from pytest import mark

@mark.asyncio
async def test_if_download_content():
	magaz.cache.delOld('magaz')
	await magaz.run()
	assert magaz.cache.exist()

@mark.asyncio
async def test_if_read_cache():
	image = await magaz.getImage()
	assert image.name

def test_if_delete_old_cache():
	magaz.cache.delOld('magaz')
	assert not magaz.cache.exist()
