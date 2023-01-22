from Modules import google

def test_if_search_google_image():
	term = 'wallpaper phone'
	google.run(term, 1)
	img = google.getImage()
	assert img.name