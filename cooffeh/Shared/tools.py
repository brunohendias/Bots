from Modules.setup import app
from Shared import message, reply
from os import popen
from datetime import datetime as dt
from secrets import token_urlsafe

def getCommand(data):
    return data.split('_')

def cacheName(name):
    now = dt.now()
    return f"{now.day}{'AM' if now.hour < 12 else 'PM'}{name}.txt"

def MegaBytesToBytes(mb: int):
    return mb * 1000000

async def clear():
    popen('rm -rf ./Contents/*')

async def progress(current, total, msg):
    await app.edit_message_text(
        msg.chat.id, 
        msg.id, 
        f"{current * 100 / total:.1f}%")

async def showSites(msg):
    return await msg.edit_message_text(
        'Click on one site under...',
        reply_markup=reply.sites())


async def preparVideo(msg, act, index, name):
    obj = act(index)
    if not obj.site:
        index = 1
        obj = act(index)
    return await msg.edit_message_text(
        message.video(obj),
        reply_markup=reply.video(index, name))

async def preparImage(msg, act, index, name):
    obj = act(index)
    if not obj.name:
        index = 1
        obj = act(index)
    return await msg.edit_message_text(
        message.image(obj),
        reply_markup=reply.carousel(index, name))

async def sendPhoto(msg, file_):
    if not file_:
        return await msg.reply('Not Found!')
    await msg.reply('Finished with success! Sending...')
    return await app.send_photo(msg.chat.id, file_)

async def sendVideo(msg, file_, caption):
    chat = msg.from_user.id
    if not file_:
        return await app.send_message(chat, 'Not Found!')
    elif file_ == 'no link':
        return await app.send_message(chat, message.nolink)
    elif file_:
        await app.send_message(chat, 'Finished with success! Sending...')
        prog = await app.send_message(chat, '0%')
        return await app.send_video(chat, file_, 
            caption=caption, 
            progress_args=[prog],
            progress=progress)
