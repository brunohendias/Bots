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

def stream(index, name):
    return KM([
        [ KB('<',f"{index-1}_{name}"),
            KB('>',f"{index+1}_{name}")],
        [ KB('Download',f"{index}_download{name}"),
            KB('Other site', '1_streams')],
    ])

def sites():
    return KM([
        [ 
            KB('XVideos', '1_xvid'),
            KB('RedTube', '1_red')
        ],[ 
            KB('PornHub', '1_hub'),
            KB('Brasileirinhas', '1_brasa')
        ]
    ])

def streams():
    return KM([
        [ 
            KB('Netflix', '1_flix'),
            KB('PrimeVideo', '1_prime')
        ]
    ])

async def start(msg, name):
    return await msg.reply(
        text='Lets show!!', 
        reply_markup=KM([[ KB('start', name) ]]))

async def option(msg, id_, text):
    return await msg.reply(
        text=text, 
        reply_markup=KM([[ 
            KB('Audio', f'{id_}_audio'),
            KB('Video', f'{id_}_video')
        ]]))
