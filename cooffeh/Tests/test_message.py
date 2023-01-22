from Shared import message
from Models.Video import Video
from Models.Image import Image

def test_if_exist_process_msg():
	assert message.process

def test_if_exist_nolink_msg():
	assert message.nolink

def test_if_exist_uploadlimite_msg():
	assert message.uploadLimite

def test_if_exist_introduce_msg():
	assert message.introduce

def test_if_exist_video_msg():
	assert 'href=' in message.video(Video())

def test_if_exist_image_msg():
	assert 'href=' in message.image(Image())

def test_if_exist_loginfo_msg():
	assert 'LOG: ' in message.loginfo(1, 
		'pytest', 'testing function')

def test_if_exist_logerr_msg():
	assert 'ERROR: ' in message.logerr(1, 
		'pytest', 'no error', 'testing function')


