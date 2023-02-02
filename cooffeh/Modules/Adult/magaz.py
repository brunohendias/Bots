from Modules.Adult import erome, play
import asyncio

async def runAsync():
    await erome.run()
    await play.run()

async def searchAsync(term: str):
    await erome.search(term)

def run():
    asyncio.run(runAsync())

def search(term: str):
    asyncio.run(searchAsync(term))