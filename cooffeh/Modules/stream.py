from Modules.Scrapper import prime, flix
import asyncio

async def runAsync():
	await prime.run()
	await flix.run()

def run():
	asyncio.run(runAsync())