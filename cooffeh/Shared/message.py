process = 'Processing...'
nolink = 'I cant get the link to download, just video with duration'
uploadLimite = 'This file is more then 50mb and exceed the upload limite'

def adult(content):
    return f'<a href="{content.thumb}">{content.site}</a>\n<a href="{content.href}">{content.title}</a>'

def magazine(content):
    return f'<a href="{content.img}">{content.name}</a>'
