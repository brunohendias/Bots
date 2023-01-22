from Modules import qrcode, youtube, instagram, video, adult, google
from Modules.Adult import magaz, red, hub, xvid
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
    
    async def showAdult(msg):
        Thread(target=adult.run).start()
        return await reply.start(msg, '1_xvid')

    async def showMagazine(msg):
        Thread(target=magaz.run).start()
        return await reply.start(msg, '1_magaz')

    async def searchGoogleImages(msg):
        term = msg.text.lower().replace('search ', '')
        Thread(target=google.run(term)).start()
        return await reply.start(msg, '1_goo')

    async def searchAdult(msg):
        term = msg.text.lower().replace('xsearch ', 
            '').replace(' ', '+')
        Thread(target=adult.search(term)).start()
        return await reply.start(msg, '1_xvid')

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
        Command('adult', showAdult),
        Command('magazine', showMagazine),
        Command('search', searchGoogleImages),
        Command('xsearch', searchAdult),
        Command('cleard', clearContents),
        Command('/start', introduce),
        Command('help', introduce)
    ]

class Callbacks:

    async def showSites(msg, index):
        return await tools.showSites(msg)

    async def xvidVideo(msg, index):
        return await tools.preparVideo(msg, 
            xvid.getVideo, index, 'xvid')

    async def hubVideo(msg, index):
        return await tools.preparVideo(msg, 
            hub.getVideo, index, 'hub')

    async def redVideo(msg, index):
        return await tools.preparVideo(msg, 
            red.getVideo, index, 'red')

    async def magazine(msg, index):
        return await tools.preparImage(msg, 
            magaz.getImage, index, 'magaz')

    async def googleImageSearch(msg, index):
        return await tools.preparImage(msg, 
            google.getImage, index, 'goo')

    async def downloadXvid(msg, index):
        resp = xvid.getLink(index)
        return await tools.sendVideo(msg,
            adult.download(resp['link']),
            resp['title'])

    async def downloadRed(msg, index):
        resp = red.getLink(index)
        return await tools.sendVideo(msg,
            adult.download(resp['link']),
            resp['title'])

    async def downloadHub(msg, index):
        resp = hub.getLink(index)
        return await tools.sendVideo(msg,
            adult.download(resp['link']),
            resp['title'])

    menu = [
        Command('sites', showSites),
        Command('xvid', xvidVideo),
        Command('hub', hubVideo),
        Command('red', redVideo),
        Command('magaz', magazine),
        Command('goo', googleImageSearch),
        Command('downloadxvid', downloadXvid),
        Command('downloadred', downloadRed),
        Command('downloadhub', downloadHub)
    ]
