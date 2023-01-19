from pyrogram.types import InlineKeyboardButton as KB
from pyrogram.types import InlineKeyboardMarkup as KM

def carousel(index, name):
    return KM([
        [ KB('<',f"{index-1}_{name}"),KB('>',f"{index+1}_{name}")],
        [ KB('Download',f"{index}_download{name}")]
    ])

def adult(i):
    return KM([
        [ KB('1', '1_adult'),KB('<', f"{i-1}_adult"),KB('>', f"{i+1}_adult") ],
        [ KB('xvideos', '1_xvid'), KB('redtube', '1_red'), KB('pornhub', '1_hub')],
        [ KB('Download', f"{i}_downloadAdult") ]
    ])

async def start(msg, name):
    return await msg.reply(
        text='Lets show!!', 
        reply_markup=KM([[ KB('start', name) ]]))
