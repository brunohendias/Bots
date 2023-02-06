from Modules.Scrapper import xvid, red, hub, brasa, erome, play
from asyncio import run as runner

async def runAsync():
    await xvid.run()
    await red.run()
    await hub.run()
    await erome.run()
    await brasa.run()
    await play.run()

async def searchAsync(term: str):
    await xvid.search(term)
    await red.search(term)
    await hub.search(term)
    await erome.search(term)
    await brasa.search(term)
    await play.run()

def run():
    runner(runAsync())

def search(term: str):
    runner(searchAsync(term))
