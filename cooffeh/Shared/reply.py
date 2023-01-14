from pyrogram.types import InlineKeyboardButton as KB
from pyrogram.types import InlineKeyboardMarkup as KM

def adult(i):
    return KM([
        [ KB('1', '0_adult'),KB('<', f"{i-1}_adult"),KB('>', f"{i+1}_adult") ],
        [ KB('Download', f"{i}_downloadAdult") ]
    ])

def magazine(i):
    return KM([
        [ KB('<', f"{i-1}_magazine"),KB('>', f"{i+1}_magazine") ]
    ])

async def start(msg, query_):
    return await msg.reply(
        text='Lets show!!', 
        reply_markup=KM([[ KB('start', query_) ]]))
