from requests import get
from bs4 import BeautifulSoup as bs

def download(text):
    html = get(text).text
    if not html:
        return ''
    soup = bs(html, 'html.parser')
    meta = soup.find('meta', {"name" : "twitter:image"})
    if not meta:
        return ''
    content = get(meta.attrs['content']).content
    if not content:
        return ''
    file_ = './Contents/image.jpg'
    with open(file_, 'wb') as f:
        f.write(content)
    return file_
