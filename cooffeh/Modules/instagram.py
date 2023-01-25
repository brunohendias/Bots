from requests import get
from bs4 import BeautifulSoup as bs
from Shared import tools

def download(text):
    html = get(text).text
    if not html:
        return ''
    soup = bs(html, 'html.parser')
    meta = soup.find('meta', {"name" : "twitter:image"})
    if not meta:
        return ''
    return tools.saveContent(meta.attrs['content'], 'jpg')