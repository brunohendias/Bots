from Modules import qrcode, youtube, instagram, adult, stream
from Modules.Adult import magaz, goo
from importlib import import_module as adt
from Models.Command import Command
from Shared import message, tools, reply
from threading import Thread

class Commands:
    
    async def randomPassword(msg):
        from secrets import token_urlsafe as token
        return await msg.reply(token(30))

    async def generateQRCode(msg):
        return await tools.sendPhoto(msg,
            qrcode.write(msg.text))

    async def downloadInstagramImagePost(msg):
        return await tools.sendPhoto(msg, 
            instagram.download(msg.text))

    async def downloadYoutubeVideo(msg):
        return await tools.sendVideo(msg,
            youtube.getVideo(msg.text),
            'Youtube video')

    async def downloadYoutubeAudio(msg):
        text = msg.text.split(' ')[1]
        return await tools.sendAudio(msg,
            youtube.getAudio(text))
    
    async def showAdult(msg):
        Thread(target=adult.run).start()
        return await reply.start(msg, '1_xvid')

    async def showMagazine(msg):
        Thread(target=magaz.run).start()
        return await reply.start(msg, '1_magaz')

    async def showStream(msg):
        Thread(target=stream.run).start()
        return await reply.start(msg, '1_flix')

    async def searchGoogleImages(msg):
        goo.run(msg.text.lower().replace('search ', ''))
        return await reply.start(msg, '1_goo')

    async def searchAdult(msg):
        term = msg.text.lower().replace(
            'xsearch ', '').replace(' ', '+')
        Thread(target=adult.search, args=[term]).start()
        return await reply.start(msg, '1_xvid')

    async def clearContents(msg):
        tools.clear()
        return await msg.reply('Done')

    async def introduce(msg):
        return await msg.reply(message.introduce)

    menu = [
        Command('password', randomPassword),
        Command('audio', downloadYoutubeAudio),
        Command('youtube', downloadYoutubeVideo),
        Command('instagram', downloadInstagramImagePost),
        Command('qrcode', generateQRCode),
        Command('adult', showAdult),
        Command('magazine', showMagazine),
        Command('stream', showStream),
        Command('search', searchGoogleImages),
        Command('xsearch', searchAdult),
        Command('cleard', clearContents),
        Command('/start', introduce),
        Command('help', introduce)
    ]

class Callbacks:

    async def showSites(msg, index, com):
        return await msg.edit_message_text(
            'Choose One Site',
            reply_markup=reply.sites())

    async def showStreams(msg, index, com):
        return await msg.edit_message_text(
            'Choose One Site',
            reply_markup=reply.streams())

    async def preparStream(msg, index, com):
        obj = adt('Modules.Stream.'+com).getVideo(index)
        return await msg.edit_message_text(
            message.video(obj),
            reply_markup=reply.stream(index, com))

    async def preparVideo(msg, index, com):
        obj = adt('Modules.Adult.'+com).getVideo(index)
        return await msg.edit_message_text(
            message.video(obj),
            reply_markup=reply.video(index, com))

    async def preparImage(msg, index, com):
        obj = adt('Modules.Adult.'+com).getImage(index)
        return await msg.edit_message_text(
            message.image(obj),
            reply_markup=reply.carousel(index, com))

    async def download(msg, index, com):
        com = com.replace('download', '')
        resp = adt('Modules.Adult.'+com).getLink(index)
        return await tools.sendVideo(msg,
            adult.download(resp['link']),
            resp['title'])

    menu = [
        Command('sites', showSites),
        Command('streams', showStreams),
        Command('xvid', preparVideo),
        Command('hub', preparVideo),
        Command('red', preparVideo),
        Command('brasa', preparVideo),
        Command('magaz', preparImage),
        Command('goo', preparImage),
        Command('flix', preparStream),
        Command('prime', preparStream),
        Command('downloadxvid', download),
        Command('downloadred', download),
        Command('downloadhub', download)
    ]
