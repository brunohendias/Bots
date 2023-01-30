from Modules import qrcode, youtube, instagram, adult, stream, option
from Modules.Adult import magaz, goo
from importlib import import_module as adt
from Models.Command import Command
from Shared import message, tools, reply

class Commands:
    
    async def randomPassword(msg):
        from secrets import token_urlsafe as token
        return await msg.reply(token(30))

    async def generateQRCode(msg):
        return await tools.sendPhoto(msg,
            qrcode.write(msg.text))

    async def downloadInstagramImagePost(msg):
        return await tools.sendPhoto(msg, 
            await instagram.download(msg.text))
    
    async def showYoutubeOptions(msg):
        return await reply.option(msg,
            option.set(msg),
            await youtube.text(msg.text))

    async def showStream(msg):
        tools.backgroundTask(stream.run)
        return await reply.start(msg, '1_flix')

    async def searchGoogleImages(msg):
        await goo.run(msg.text.lower().replace('search ', ''))
        return await reply.start(msg, '1_goo')

    async def introduce(msg):
        return await msg.reply(message.introduce)

    menu = [
        Command('password', randomPassword),
        Command('youtube', showYoutubeOptions),
        Command('instagram', downloadInstagramImagePost),
        Command('qrcode', generateQRCode),
        Command('stream', showStream),
        Command('search', searchGoogleImages),
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

    async def downloadYoutubeVideo(msg, index, com):
        opt = option.get(index)
        return await tools.sendVideo(msg,
            youtube.getVideo(opt.text),
            'Youtube Video')
    
    async def downloadYoutubeAudio(msg, index, com):
        opt = option.get(index)
        return await tools.sendAudio(msg,
            youtube.getAudio(opt.text))

    async def preparStream(msg, index, com):
        obj = await adt('Modules.Stream.'+com).getVideo(index)
        return await msg.edit_message_text(
            message.video(obj),
            reply_markup=reply.stream(index, com))

    async def preparVideo(msg, index, com):
        obj = await adt('Modules.Adult.'+com).getVideo(index)
        return await msg.edit_message_text(
            message.video(obj),
            reply_markup=reply.video(index, com))

    async def preparImage(msg, index, com):
        obj = await adt('Modules.Adult.'+com).getImage(index)
        return await msg.edit_message_text(
            message.image(obj),
            reply_markup=reply.carousel(index, com))

    async def download(msg, index, com):
        com = com.replace('download', '')
        resp = await adt('Modules.Adult.'+com).getLink(index)
        return await tools.sendVideo(msg,
            await adult.download(resp['link']),
            resp['title'])

    menu = [
        Command('sites', showSites),
        Command('streams', showStreams),
        Command('video', downloadYoutubeVideo),
        Command('audio', downloadYoutubeAudio),
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

class Own:

    async def showAdult(msg):
        tools.backgroundTask(adult.run)
        return await reply.start(msg, '1_xvid')

    async def showMagazine(msg):
        tools.backgroundTask(magaz.run)
        return await reply.start(msg, '1_magaz')

    async def searchAdult(msg):
        term = msg.text.lower().replace(
            'xsearch ', '').replace(' ', '+')
        tools.backgroundTask(adult.search, [term])
        return await reply.start(msg, '1_xvid')

    async def clearContents(msg):
        tools.clear()
        return await msg.reply('Done')

    menu = [
        Command('adult', showAdult),
        Command('magazine', showMagazine),
        Command('xsearch', searchAdult),
        Command('cleard', clearContents)
    ]