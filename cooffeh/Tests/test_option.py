from Modules import option

class User:
	id = 1

class Msg:
	from_user = User()
	text = 'https://testandocreateoption.com'

def test_if_set_option():
	assert option.set(Msg()) >= 0

def test_if_get_option():
	assert option.get(0).text
