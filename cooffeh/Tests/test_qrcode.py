from Modules import qrcode
from os import path

def test_if_generate_qrcode():
	text = 'https://github.com/brunohendias'
	resp = qrcode.write(text)
	assert len(resp) > 0 and path.exists(resp)
