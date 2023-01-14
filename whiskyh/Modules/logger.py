from datetime import date

def info(user, iduser, msg):
    with open('./Log/log.txt', 'at+') as f:
        f.write(f"LOG: {date.today()}\nUsr: {user}-{iduser}\nMsg: {msg}\n\n")

def debug(text):
    with open('./Log/debug.txt', 'at+') as f:
        f.write(f"DEBUGGER: {date.today()}\n{text}\n\n")

def error(e, user, iduser, msg):
    with open('./Log/error.txt', 'at+') as f:
        f.write(f"ERROR: {date.today()}\n{e}\nUsr: {user}-{iduser}\nMsg: {msg}\n\n")