from Shared import reply

def test_if_create_carousel_keyboard():
	assert reply.carousel(1, 'goo')

def test_if_create_video_keyboard():
	assert reply.video(1, 'goo')

def test_if_create_sites_keyboard():
	assert reply.sites()


