from Modules.setup import app, KM, KB
from Modules.youtube import Youtube
from Modules.instagram import Instagram
from Modules.qrcode_ import QRCode
from Modules.video import Video
from Modules.adult import Adult
from Modules.magazine import Magazine
from Models.Command import Command
from Models.List import List
from secrets import token_urlsafe as passw
com = List()
msuccess = 'Finished with success! Sending...'
mfail = 'Not Found!'

async def progress(current, total, msg):
    await app.edit_message_text(msg.chat.id, 
        msg.id, 
        f"{current * 100 / total:.1f}%")

class Commands():
    
    async def randomPassword(msg):
        await msg.reply('Generating the password...')
        return await msg.reply(passw(50))

    async def generateQRCode(msg):
        await msg.reply('Generating the qrcode...')
        f = QRCode().write(msg.text.split(' ')[1])
        if not f:
            return await msg.reply(mfail)
        await msg.reply(msuccess)
        return await app.send_photo(msg.chat.id, f)

    async def downloadYoutubeVideo(msg):
        await msg.reply('Downloading video...')
        f = Youtube().downloadVideo(msg)
        if not f:
            return await msg.reply(mfail)
        await msg.reply(msuccess)
        return await app.send_video(msg.chat.id, f)

    async def downloadInstagramImagePost(msg):
        await msg.reply('Downloading image...')
        f = Instagram().downloadImagePost(msg)
        if not f:
            return await msg.reply(mfail)
        await msg.reply(msuccess)
        return await app.send_photo(msg.chat.id, f)

    async def videoMP4Download(msg):
        await msg.reply('Downloading video...')
        f = Video().downloadMP4(msg.text)
        if not f:
            return await msg.reply(mfail)
        await msg.reply(msuccess)
        return await app.send_video(msg.chat.id, f)
    
    async def showAdultCallback(msg):
        return await msg.reply('Lets show!!', 
            reply_markup=KM([[ KB('start', '0_adult') ]]))

    async def showMagazineCallback(msg):
        return await msg.reply('Lets show!!', 
            reply_markup=KM([[ KB('start', '0_magazine') ]]))

    menu = [
        Command(com.password, randomPassword),
        Command(com.youtube, downloadYoutubeVideo),
        Command(com.instagram, downloadInstagramImagePost),
        Command(com.qrcode, generateQRCode),
        Command(com.videomp4, videoMP4Download),
        Command(com.adult, showAdultCallback),
        Command(com.magazine, showMagazineCallback)
    ]

class Callbacks():
    async def adultVideo(msg):
        i = int(msg.data.split('_')[0])
        content = Adult().run(i)
        if not content.title:
            return await app.send_message(msg.from_user.id, mfail)
        text = f'<a href="{content.thumb}">{content.title}</a>'
        buttons = [
            [ KB('<', f"{i-1}_adult"),KB('>', f"{i+1}_adult") ],
            [ KB('Download', f"{i}_downloadAdult") ]
        ]
        return await msg.edit_message_text(text, reply_markup=KM(buttons))

    async def downloadAdultVideo(msg):
        chat = msg.from_user.id
        i = int(msg.data.split('_')[0])
        video = Adult().run(i)
        await app.send_message(chat, 'Downloading video...')
        f = Adult().download(video.href)
        if f:
            await app.send_message(chat, msuccess)
            msgprog = await app.send_message(chat, '0%')
            return await app.send_video(chat, f, 
                caption=video.title, 
                protect_content=True,
                progress_args=[msgprog],
                progress=progress)
        elif f == 'no link':
            await app.send_message(chat, 
                'Videos without duration i cant get the link')
            return await app.send_message(chat, 
                f"Its the video page link {video.href}")
        else:
            return await app.send_message(chat, mfail)

    async def magazineImage(msg):
        i = int(msg.data.split('_')[0])
        content = Magazine().run(i)
        if not content.name:
            return await app.send_message(msg.from_user.id, mfail)
        text = f'<a href="{content.img}">{content.name}</a>'
        return await msg.edit_message_text(text, reply_markup=KM([
            [ KB('<', f"{i-1}_magazine"),KB('>', f"{i+1}_magazine") ]
        ]))

    menu = [
        Command(com.adult, adultVideo),
        Command(com.downloadAdult, downloadAdultVideo),
        Command(com.magazine, magazineImage)
    ]
