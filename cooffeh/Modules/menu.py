from Modules import qrcode_, youtube, instagram, video, adult
from Modules.Adult import magazine
from Models import Command, List
from Shared import message, tools, reply
from threading import Thread

class Commands:
    
    async def randomPassword(msg):
        await msg.reply(message.process)
        return await msg.reply(tools.token_urlsafe(40))

    async def generateQRCode(msg):
        await msg.reply(message.process)
        return await tools.sendPhoto(msg,
            qrcode_.write(msg.text))

    async def downloadInstagramImagePost(msg):
        await msg.reply(message.process)
        return await tools.sendPhoto(msg, 
            instagram.download(msg.text))

    async def downloadYoutubeVideo(msg):
        await msg.reply(message.process)
        return await tools.sendVideo(msg,
            youtube.download(msg.text),
            'Youtube video')

    async def videoMP4Download(msg):
        await msg.reply(message.process)
        return await tools.sendVideo(msg,
            video.downloadMP4(msg.text),
            'MP4 video')
    
    async def showAdultCallback(msg):
        Thread(target=adult.run(), name="writeCache").start()
        return await reply.start(msg, '0_adult')

    async def showMagazineCallback(msg):
        Thread(target=magazine.run(), name="writeCache").start()
        return await reply.start(msg, '0_magazine')

    menu = [
        Command.add(List.con.password, randomPassword),
        Command.add(List.con.youtube, downloadYoutubeVideo),
        Command.add(List.con.instagram, downloadInstagramImagePost),
        Command.add(List.con.qrcode, generateQRCode),
        Command.add(List.con.videomp4, videoMP4Download),
        Command.add(List.con.adult, showAdultCallback),
        Command.add(List.con.magazine, showMagazineCallback)
    ]

class Callbacks:
    async def adultVideo(msg, index):
        content = adult.getVideo(index)
        return await msg.edit_message_text(
            text=message.adult(content),
            reply_markup=reply.adult(index))

    async def downloadAdultVideo(msg, index):
        content = adult.getVideo(index)
        return await tools.sendVideo(msg,
            adult.download(content.href, content.link), 
            content.title)

    async def magazineImage(msg, index):
        content = magazine.getImage(index)
        return await msg.edit_message_text(
            text=message.magazine(content),
            reply_markup=reply.magazine(index))

    menu = [
        Command.add(List.con.adult, adultVideo),
        Command.add(List.con.downloadAdult, downloadAdultVideo),
        Command.add(List.con.magazine, magazineImage)
    ]
