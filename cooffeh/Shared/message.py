success = 'Finished with success! Sending...'
fail = 'Not Found!'
process = 'Processing...'
nolink = 'I cant get the link to download, just video with duration'
uploadLimite = 'This file is more then 50mb and exceed the upload limite'

def adult(content):
    return f'{content.site}\nName <a href="{content.thumb}">{content.title}</a>\nVideo <a href="{content.href}">link</a>'

def magazine(content):
    return f'<a href="{content.img}">{content.name}</a>'