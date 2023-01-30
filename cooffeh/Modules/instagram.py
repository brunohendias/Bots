from Shared import tools

async def download(text):
    soup = await tools.getSoup(text)
    meta = soup.find('meta', {"name" : "twitter:image"})
    if not meta:
        return ''
    return await tools.saveContent(meta.attrs['content'], 'jpg')