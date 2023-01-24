from Modules import qrcode
from os import path

def test_if_generate_qrcode():
	text = 'https://github.com/brunohendias'
	assert path.exists(qrcode.write(text))
