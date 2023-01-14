from requests import get
from bs4 import BeautifulSoup as bs
from Modules.renderhtml import RenderHTML

class Video:
    def downloadMP4(self, url):
        if not url:
            return ''
        elif 'https://www.google.com/url?' in url:
            try:
                redirect = str.encode(str(get(url).content).replace('\\xe', ''))
                url = str(bs(redirect, 'html.parser').find('a')['href'])
            except Exception as err:
                return err

        links = []
        ltags = []
        content = RenderHTML().render(url)
        soup = bs(content, 'html.parser')
        ltags.append(soup.find_all('source'))
        ltags.append(soup.find_all('video'))
        for tags in ltags:
            for tag in tags:
                try:
                    if '.mp4' in tag['src']:
                        links.append(tag['src'])
                    elif 'mp4' in tag['type']:
                        links.append(tag['src'])
                except:
                    pass
        
        if len(links) == 0:
            for tag in soup.find_all('a'):
                if '.mp4' in tag['href']:
                    links.append(tag['href'])

        if len(links) > 0:
            link = links[len(links) - 1]
        else:
            return ''
        
        output = './Contents/video.mp4'
        video = get(link).content
        if not video:
            return ''
        
        with open(output, 'wb') as f:
            f.write(video)
            f.close()

        return output

def downloadMP4(url):
    return Video().downloadMP4(url)