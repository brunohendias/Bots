process = 'Processing...'
nolink = 'I cant get the link to download, just video with duration'
uploadLimite = 'This file is more then 50mb and exceed the upload limite'

def video(obj):
    return f'<a href="{obj.thumb}">{obj.site}</a>\n<a href="{obj.href}">{obj.title}</a>'

def image(obj):
    return f'<a href="{obj.img}">{obj.site}</a>\n<a href="{obj.page}">{obj.name}</a>'

def loginfo(id, user, text):
    return f"LOG: {id}\nUser: {user}\nMsg: {text}"

def logerr(id, user, err):
    return f"ERROR: {id}\nUser: {user}\n{err}"