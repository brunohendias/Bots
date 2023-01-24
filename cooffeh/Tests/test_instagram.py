from Modules import instagram
from os import path

def test_if_download_instagram_post():
	text = 'https://www.instagram.com/p/Cno_NenuI_R'
	assert path.exists(instagram.download(text))

def test_if_return_empty_url_notfound():
	text = 'https://www.instagram.com/p/dawdwadaw'
	assert not path.exists(instagram.download(text))
