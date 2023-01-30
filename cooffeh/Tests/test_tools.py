from Shared import tools
from os import path
from pytest import mark

def test_if_get_callback_command():
	assert tools.getCommand('1_goo')

def test_if_create_cache_name():
	assert 'test.txt' in tools.cacheName('test')

def test_if_convert_megabytes_to_bytes():
	assert tools.megaBytesToBytes(50) == 52428800

def test_if_clear_contents_folder():
	file_ = './Contents/test.txt'
	with open(file_, 'wt') as f:
		f.write('teste')
	tools.clear()
	with open('./Contents/nocontent', 'wt') as f:
		f.write('nothing')
	assert not path.exists(file_)

@mark.asyncio
async def test_if_create_html_soup():
	assert await tools.getSoup('https://github.com')

# def test_if_save_file_content():
# 	assert path.exists(tools.saveContent('', 'mp3'))
