from Models.Video import Video
from bs4 import BeautifulSoup as bs
from requests import get

def run(cache):
    basepath = 'https://pt.pornhub.com'
    html = get(basepath).text
    if not html:
        return ''
    soup = bs(html, 'html.parser')
    tags = soup.find_all('li', 'pcVideoListItem')
    for tag in tags:
        a = tag.find('a')
        if not a:
            pass
        video = Video()
        video.site = 'PornHub'
        video.title = a.attrs['title']
        video.href = basepath + a.attrs['href']
        video.thumb = a.find('img').attrs['src']
        cache.writeline(video)
