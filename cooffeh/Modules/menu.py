from Modules import qrcode, youtube, instagram, video, adult, google
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
        tools.backgroundTask(adult.run())
        return await reply.start(msg, '1_adult')

    async def showMagazineCallback(msg):
        tools.backgroundTask(magazine.run())
        return await reply.start(msg, '1_magazine')

    async def searchGoogleImagesCallback(msg):
        term = msg.text.lower().replace('search ', '')
        tools.backgroundTask(google.searchImages(term))
        return await reply.start(msg, '1_google')

    async def clearContents(msg):
        return await tools.clear()

    async def introduce(msg):
        return await msg.reply(message.introduce())

    menu = [
        Command('password', randomPassword),
        Command('youtube', downloadYoutubeVideo),
        Command('instagram', downloadInstagramImagePost),
        Command('qrcode', generateQRCode),
        Command('videomp4', videoMP4Download),
        Command('adult', showAdultCallback),
        Command('magazine', showMagazineCallback),
        Command('search', searchGoogleImagesCallback),
        Command('cleard', clearContents),
        Command('/start', introduce),
        Command('help', introduce),
    ]

class Callbacks:
    async def adultVideo(msg, index):
        obj = adult.getVideo(index)
        if not obj.site:
            index = 1
            obj = adult.getVideo(1)
        return await msg.edit_message_text(
            message.video(obj),
            reply_markup=reply.adult(index))

    async def downloadAdultVideo(msg, index):
        obj = adult.getVideo(index)
        return await tools.sendVideo(msg,
            adult.download(obj.href, obj.link),
            obj.title)

    async def magazineImage(msg, index):
        obj = magazine.getImage(index)
        if not obj.name:
            index = 1
            obj = magazine.getImage(1)
        return await msg.edit_message_text(
            message.image(obj),
            reply_markup=reply.magazine(index))

    async def googleImageSearch(msg, index):
        obj = google.getImage(index)
        if not obj.name:
            index = 1
            obj = google.getImage(1)
        return await msg.edit_message_text(
            message.image(obj),
            reply_markup=reply.google(index))

    menu = [
        Command('adult', adultVideo),
        Command('downloadAdult', downloadAdultVideo),
        Command('magazine', magazineImage),
        Command('google', googleImageSearch),
    ]
