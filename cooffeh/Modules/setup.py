from os import getenv, path, mkdir
from dotenv import load_dotenv
from pyrogram import Client

if not path.exists('Contents'):
    mkdir('Contents')

load_dotenv()
admin = int(getenv('TELEGRAM_ADMIN_ID'))
app = Client(
    getenv('TELEGRAM_API_BOTNAME'),
    api_id=getenv('TELEGRAM_API_ID'),
    api_hash=getenv('TELEGRAM_API_HASH'),
    bot_token=getenv('TELEGRAM_API_TOKEN')
)
