from Modules import instagram
from os import path

def test_if_download_instagram_post():
	text = 'https://www.instagram.com/p/Cno_NenuI_R'
	resp = instagram.download(text)
	assert len(resp) > 0 and path.exists(resp)

def test_if_return_empty_url_notfound():
	text = 'https://www.instagram.com/p/dawdwadaw'
	resp = instagram.download(text)
	assert len(resp) == 0 and not path.exists(resp)
