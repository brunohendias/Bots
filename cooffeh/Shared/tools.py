from Modules.setup import app
from Shared import message
from secrets import token_urlsafe
from os import popen
from datetime import datetime as dt
from threading import Thread

def getCommand(data):
    return data.split('_')

def cacheName(name):
    now = dt.now()
    return f"{now.day}{'AM' if now.hour < 12 else 'PM'}{name}.txt"

def backgroundTask(run):
    return Thread(target=run()).start()

async def clear():
    popen('rm -rf ./Contents/*')

async def progress(current, total, msg):
    await app.edit_message_text(
        msg.chat.id, 
        msg.id, 
        f"{current * 100 / total:.1f}%")

async def sendPhoto(msg, file_):
    if not file_:
        return await msg.reply('Not Found!')
    await msg.reply('Finished with success! Sending...')
    return await app.send_photo(msg.chat.id, file_)

async def sendVideo(msg, file_, caption):
    chat = msg.from_user.id
    if file_ == 'no link':
        return await app.send_message(chat, 
            message.nolink)
    elif file_ == 'file size':
        return await app.send_message(chat, 
            message.uploadLimite)
    elif file_:
        await app.send_message(chat, 'Finished with success! Sending...')
        prog = await app.send_message(chat, '0%')
        return await app.send_video(chat, file_, 
            caption=caption, 
            protect_content=True,
            progress_args=[prog],
            progress=progress)
    else:
        return await app.send_message(chat, 'Not Found!')
