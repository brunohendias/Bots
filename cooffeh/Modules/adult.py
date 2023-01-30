from Modules.Adult import xvid, red, hub, brasa
from Shared import tools
import asyncio

async def runAsync():
    await xvid.run()
    await hub.run()
    await red.run()
    await brasa.run()

async def searchAsync(term: str):
    await xvid.search(term)
    await red.search(term)
    await hub.search(term)
    await brasa.search(term)

async def download(link: str):
    return await tools.saveContent(link, 'mp4')

def run():
    asyncio.run(runAsync())

def search(term: str):
    asyncio.run(searchAsync(term))
