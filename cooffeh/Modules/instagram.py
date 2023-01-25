from Shared import tools

def download(text):
    soup = tools.getSoup(text)
    meta = soup.find('meta', {"name" : "twitter:image"})
    if not meta:
        return ''
    return tools.saveContent(meta.attrs['content'], 'jpg')