from Shared import tools
from os import path

def test_if_get_callback_command():
	assert len(tools.getCommand('1_goo')) > 1

def test_if_create_cache_name():
	assert 'test.txt' in tools.cacheName('test')

def test_if_covert_megabytes_to_bytes():
	assert tools.megaBytesToBytes(50) == 50000000

def test_if_clear_contents_folder():
	file_ = './Contents/test.txt'
	with open(file_, 'wt') as f:
		f.write('teste')
	tools.clear()
	assert not path.exists(file_)
