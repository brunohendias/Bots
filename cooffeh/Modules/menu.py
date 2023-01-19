from Modules import qrcode, youtube, instagram, video, adult, google
from Modules.Adult import magazine, red, hub, xvid
from Models.Command import Command
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
        Thread(target=adult.run).start()
        return await reply.start(msg, '1_adult')

    async def showMagazineCallback(msg):
        Thread(target=magazine.run).start()
        return await reply.start(msg, '1_magazine')

    async def searchGoogleImagesCallback(msg):
        term = msg.text.lower().replace('search ', '')
        Thread(target=google.searchImages(term), cacheName='writeCache').start()
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
        return await tools.preparVideo(msg, 
            adult.getVideo, index)

    async def xvidVideo(msg, index):
        return await tools.preparVideo(msg, 
            xvid.getVideo, index)

    async def hubVideo(msg, index):
        return await tools.preparVideo(msg, 
            hub.getVideo, index)

    async def redVideo(msg, index):
        return await tools.preparVideo(msg, 
            red.getVideo, index)

    async def magazineImage(msg, index):
        return await tools.preparImage(msg, 
            magazine.getImage, index, 'magaz')

    async def googleImageSearch(msg, index):
        return await tools.preparImage(msg, 
            google.getImage, index, 'goo')

    async def downloadAdultVideo(msg, index):
        obj = adult.getVideo(index)
        return await tools.sendVideo(msg,
            adult.download(obj.href, obj.link),
            obj.title)

    menu = [
        Command('adult', adultVideo),
        Command('xvid', xvidVideo),
        Command('red', redVideo),
        Command('hub', hubVideo),
        Command('magaz', magazineImage),
        Command('goo', googleImageSearch),
        Command('downloadAdult', downloadAdultVideo),
    ]
