process = 'Processing...'
nolink = 'I cant get the link to download, just video with duration'
uploadLimite = 'This file is more then 50mb and exceed the upload limite'

def video(obj):
    return f'<a href="{obj.thumb}">{obj.site}</a>\n<a href="{obj.href}">{obj.title}</a>'

def image(obj):
    return f'<a href="{obj.img}">{obj.site}</a>\n<a href="{obj.page}">{obj.name}</a>'

def loginfo(id_, user, text):
    return f"LOG: {id_}\nUser: {user}\nMsg: {text}"

def logerr(id_, user, err, text):
    return f"ERROR: {id_}\nUser: {user}\n{err}\n{text}"

introduce = """
Welcome to the bot world
With me you can:
- Download Youtube video/audio 
    sending the link
- Download Instagram image post 
    sending the link
- Generate long and strong random password 
    sending password
- Generate QRCode 
    sending "qrcode https://github.com/brunohendias"
- Download Video on website 
    sending the website link
I have a upload limite so, i just can send media up to 50mb
If do you want to see this message again send help
I hope you enjoy!
"""