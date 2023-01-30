from Modules import instagram
from os import path
from pytest import mark

@mark.asyncio
async def test_if_download_instagram_post():
	text = 'https://www.instagram.com/p/Cno_NenuI_R'
	assert path.exists(await instagram.download(text))

@mark.asyncio
async def test_if_return_empty_url_notfound():
	text = 'https://www.instagram.com/p/dawdwadaw'
	assert not path.exists(await instagram.download(text))
