from Modules import qrcode, youtube, instagram, video, adult
from Modules.Adult import magazine
from Models import Command
from Shared import message, tools, reply
from threading import Thread

class Commands:
    
    async def randomPassword(msg):
        return await msg.reply(tools.token_urlsafe(40))

    async def generateQRCode(msg):
        return await tools.sendPhoto(msg,
            qrcode.write(msg.text))

    async def downloadInstagramImagePost(msg):
        return await tools.sendPhoto(msg, 
            instagram.download(msg.text))

    async def downloadYoutubeVideo(msg):
        return await tools.sendVideo(msg,
            youtube.download(msg.text),
            'Youtube video')

    async def videoMP4Download(msg):
        return await tools.sendVideo(msg,
            video.downloadMP4(msg.text),
            'MP4 video')
    
    async def showAdultCallback(msg):
        Thread(target=adult.run(), name="writeCache").start()
        return await reply.start(msg, '1_adult')

    async def showMagazineCallback(msg):
        Thread(target=magazine.run(), name="writeCache").start()
        return await reply.start(msg, '1_magazine')

    async def clearContents(msg):
        return await tools.clear()

    menu = [
        Command.add('password', randomPassword),
        Command.add('youtube', downloadYoutubeVideo),
        Command.add('instagram', downloadInstagramImagePost),
        Command.add('qrcode', generateQRCode),
        Command.add('videomp4', videoMP4Download),
        Command.add('adult', showAdultCallback),
        Command.add('magazine', showMagazineCallback),
        Command.add('cleard', clearContents),
    ]

class Callbacks:
    async def adultVideo(msg, index):
        content = adult.getVideo(index)
        if not content.site:
            index = 1
            content = adult.getVideo(1)
        return await msg.edit_message_text(
            message.adult(content),
            reply_markup=reply.adult(index))

    async def downloadAdultVideo(msg, index):
        content = adult.getVideo(index)
        return await tools.sendVideo(msg,
            adult.download(content.href, content.link),
            content.title)

    async def magazineImage(msg, index):
        content = magazine.getImage(index)
        if not content.name:
            index = 1
            content = magazine.getImage(1)
        return await msg.edit_message_text(
            message.magazine(content),
            reply_markup=reply.magazine(index))

    menu = [
        Command.add('adult', adultVideo),
        Command.add('downloadAdult', downloadAdultVideo),
        Command.add('magazine', magazineImage)
    ]
