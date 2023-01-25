from Modules.Adult import xvid, red, hub, brasa
from Shared import tools

def run():
    xvid.run()
    hub.run()
    red.run()
    brasa.run()

def search(term: str):
    xvid.search(term)
    red.search(term)
    hub.search(term)
    brasa.search(term)

def download(link: str):
    return tools.saveContent(link, 'mp4')