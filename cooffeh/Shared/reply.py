from pyrogram.types import InlineKeyboardButton as KB, InlineKeyboardMarkup as KM

def carousel(index, name):
    return KM([
        [ KB('<',f"{index-1}_{name}"),
            KB('>',f"{index+1}_{name}")]
    ])

def video(index, name):
    return KM([
        [ KB('<',f"{index-1}_{name}"),
            KB('>',f"{index+1}_{name}")],
        [ KB('Download',f"{index}_download{name}"),
            KB('Other site', '1_sites')],
    ])

def sites():
    return KM([
        [ KB('xvideos', '1_xvid'),
            KB('redtube', '1_red'),
            KB('pornhub', '1_hub')]
    ])

async def start(msg, name):
    return await msg.reply(
        text='Lets show!!', 
        reply_markup=KM([[ KB('start', name) ]]))
