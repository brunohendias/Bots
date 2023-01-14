from Modules import qrcode, youtube, instagram, video, adult
from Modules.Adult import magazine
from Models.Command import Command
from Shared import message, tools, reply

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
        tools.backgroundTask(adult.run)
        return await reply.start(msg, '1_adult')

    async def showMagazineCallback(msg):
        tools.backgroundTask(magazine.run)
        return await reply.start(msg, '1_magazine')

    async def clearContents(msg):
        return await tools.clear()

    menu = [
        Command('password', randomPassword),
        Command('youtube', downloadYoutubeVideo),
        Command('instagram', downloadInstagramImagePost),
        Command('qrcode', generateQRCode),
        Command('videomp4', videoMP4Download),
        Command('adult', showAdultCallback),
        Command('magazine', showMagazineCallback),
        Command('cleard', clearContents),
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
        Command('adult', adultVideo),
        Command('downloadAdult', downloadAdultVideo),
        Command('magazine', magazineImage)
    ]
