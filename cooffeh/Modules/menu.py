from Modules import qrcode, youtube, instagram, adult, stream, option
from Modules.Scrapper import goo
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
        return await reply.start(msg, '0_flix')

    async def searchGoogleImages(msg):
        await goo.run(tools.traitTerm(msg.text, 'search '))
        return await reply.start(msg, '0_goo')

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

    async def sites(self, msg, com:str):
        return await msg.edit_message_text(
            'Choose One Site',
        reply_markup=reply.sites(com))

    async def downloadYoutubeVideo(msg, index:int, com:str):
        opt = option.get(index)
        return await tools.sendVideo(msg,
            youtube.getVideo(opt.text),
            'Youtube Video')
    
    async def downloadYoutubeAudio(msg, index:int, com:str):
        opt = option.get(index)
        return await tools.sendAudio(msg,
            youtube.getAudio(opt.text))

    async def navigate(self, msg, index:int, com:str):
        obj = adt(f'Modules.Scrapper.{com}').cache.read(index)
        return await msg.edit_message_text(
            message.content(obj),
            reply_markup=reply.navigate(index, com))

    menu = [
        Command('video', downloadYoutubeVideo),
        Command('audio', downloadYoutubeAudio)
    ]

class Own:

    async def showAdult(msg):
        tools.backgroundTask(adult.run)
        return await reply.start(msg, '0_xvid')

    async def searchAdult(msg):
        tools.backgroundTask(adult.search, 
            [tools.traitTerm(msg.text, 'xsearch ')])
        return await reply.start(msg, '0_xvid')

    menu = [
        Command('adult', showAdult),
        Command('xsearch', searchAdult)
    ]