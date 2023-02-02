from Modules.setup import app
from Shared import message
from os import system
from datetime import datetime as dt
from bs4 import BeautifulSoup as bs
from random import choices
from requests import get
from threading import Thread
from time import sleep

def getCommand(data):
    return data.split('_')

def fileName():
    return ''.join(choices('abcdefghijklm', k=3))

def cacheName(name: str):
    now = dt.now()
    return f"{now.day}{'AM' if now.hour < 12 else 'PM'}{name}.txt"

def megaBytesToBytes(mb: int):
    return mb * 1048576

def clear():
    system('rm -rf ./Contents/*')

def traitTerm(text: str, com: str):
    return text.lower().replace(
        com, '').replace(' ', '+')

def backgroundTask(action, args=[]):
    Thread(target=action, args=args).start()
    return sleep(0.5)

async def getSoup(link: str):
    if not link:
        return ''
    html = get(link).text
    return bs(html, 'html.parser')

async def saveContent(link: str, extension: str):
    if not link:
        return ''
    content = get(link).content
    if len(content) > megaBytesToBytes(50):
        return ''
    file_ = f'./Contents/{fileName()}.{extension}'
    with open(file_, 'wb') as f:
        f.write(content)
    return file_

async def progress(current, total, msg):
    await app.edit_message_text(
        msg.chat.id, 
        msg.id, 
        f"{current * 100 / total:.1f}%")

async def sendPhoto(msg, file_: str):
    if not file_:
        return await msg.reply('Not Found!')
    await msg.reply('Finished with success! Sending...')
    await app.send_photo(msg.chat.id, file_)
    return system(f'rm -rf {file_}')

async def sendAudio(msg, audio):
    chat = msg.from_user.id
    if audio.file_:
        await app.send_message(chat, f'[Thumb]({audio.thumb})\nFinished with success! Sending...')
        await app.send_audio(chat, audio.file_, 
            title=audio.title,
            performer=audio.author,
            duration=audio.duration)
        return system(f'rm -rf {audio.file_}')
    return await app.send_message(chat, 'Not Found!')

async def sendVideo(msg, file_: str, caption: str):
    chat = msg.from_user.id
    if not file_:
        return await app.send_message(chat, 'Not Found!')
    elif file_ == 'no link':
        return await app.send_message(chat, message.nolink)
    elif file_:
        await app.send_message(chat, 'Finished with success! Sending...')
        prog = await app.send_message(chat, '0%')
        await app.send_video(chat, file_, 
            caption=caption, 
            progress_args=[prog],
            progress=progress)
        return system(f'rm -rf {file_}')
