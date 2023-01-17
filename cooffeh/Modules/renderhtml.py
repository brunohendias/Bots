from scrapingant_client import ScrapingAntClient
from os import getenv

def render(url):
    client = ScrapingAntClient(token=getenv('SCRAPING_API_TOKEN'))
    return client.general_request(url).content
