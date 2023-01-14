from scrapingant_client import ScrapingAntClient
from os import getenv
from dotenv import load_dotenv

class RenderHTML:
    def render(self, url):
        load_dotenv()
        client = ScrapingAntClient(token=getenv('SCRAPING_API_TOKEN'))
        return client.general_request(url).content
