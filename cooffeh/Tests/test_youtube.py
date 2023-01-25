from Modules import youtube
from os import path

def test_if_download_youtube_video():
	text = 'https://www.youtube.com/watch?v=tPEE9ZwTmy0'
	assert path.exists(youtube.getVideo(text))

def test_if_download_youtube_audio():
	text = 'https://youtu.be/vVXIK1xCRpY'
	assert path.exists(youtube.getAudio(text).file_)
