from os import getenv, path
from dotenv import load_dotenv as load

def test_if_env_file_exist():
	assert path.exists('.env')

def test_if_envs_exist():
	load()
	for env in ['TELEGRAM_API_ID','TELEGRAM_API_HASH',
		'TELEGRAM_API_TOKEN','TELEGRAM_API_BOTNAME',
		'TELEGRAM_ADMIN_ID','SCRAPING_API_TOKEN',
		'GOOGLE_API_KEY','GOOGLE_API_CX']:
		assert getenv(env)
