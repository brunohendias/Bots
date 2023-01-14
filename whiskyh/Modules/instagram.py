from requests import get
from bs4 import BeautifulSoup as bs

class Instagram():
    def downloadImagePost(self, msg):
        html = get(msg.text).text
        if not html:
            return ''
        meta = bs(html, 'html.parser').find('meta', {"name" : "twitter:image"})
        if not meta:
            return ''
        content = get(meta.attrs['content']).content
        if not content:
            return ''
        file_ = './Contents/image.jpg'
        with open(file_, 'wb') as f:
            f.write(content)
        return file_
