from Modules import youtube
from os import path

def test_if_download_youtube_video():
	text = 'https://www.youtube.com/watch?v=tPEE9ZwTmy0'
	resp = youtube.download(text)
	assert len(resp) > 0 and path.exists(resp)
