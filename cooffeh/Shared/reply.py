from pyrogram.types import InlineKeyboardButton as KB, InlineKeyboardMarkup as KM

def navigate(index: int, name: str):
    return KM([[
        KB('<',f"{index-1}_{name}"),
        KB('>',f"{index+1}_{name}")],[
        KB('Other site', f"0_{name}sites")
    ]])

def adult():
    return KM([[ 
        KB('XVideos', '0_xvid'),
        KB('RedTube', '0_red')
    ],[ 
        KB('PornHub', '0_hub'),
        KB('Brasileirinhas', '0_brasa')
    ],[
        KB('Erome', '0_erome'),
        KB('Playboy', '0_play')
    ]])

def streams():
    return KM([[ 
        KB('Netflix', '0_flix'),
        KB('PrimeVideo', '0_prime')
    ]])

def sites(com):
    if com == 'flixsites' or com == 'primesites':
        return streams()
    return adult()

async def start(msg, name:str):
    return await msg.reply(
        text='Lets show!!',
        reply_markup=KM([[ KB('start', name) ]]))

async def option(msg, id_, text:str):
    return await msg.reply(
        text=text, 
        reply_markup=KM([[
            KB('Audio', f'{id_}_audio'),
            KB('Video', f'{id_}_video')
        ]]))
