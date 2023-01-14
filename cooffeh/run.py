from Modules.menu import List, Callbacks, Commands
from Modules.logger import info, error
from Modules.setup import app
from Shared.tools import getCommand
    
@app.on_callback_query()
async def callback(client, msg):
    usr = msg.from_user
    info(usr.first_name, usr.id, msg.data)
    try:
        call = getCommand(msg.data)
        for c in Callbacks().menu:
            if call[1] == c.command:
                return await c.action(msg, int(call[0]))
    except Exception as err:
        error(err, usr.first_name, usr.id, msg.data)

@app.on_message()
async def message(cliente, msg):
    usr = msg.from_user
    info(usr.first_name, usr.id, msg.text)
    try:
        lower = msg.text.lower()
        if "youtu.be" in lower or "www.youtube.com" in lower:
            lower = List.con.youtube
        elif "instagram.com" in lower and 'scontent.cdninstagram.com' not in lower:
            lower = List.con.instagram
        elif 'qrcode' in lower:
            lower = List.con.qrcode
        elif 'https://' in lower or 'http://' in lower:
            lower = List.con.videomp4

        for commmand in Commands().menu:
            if commmand.command == lower:
                return await commmand.action(msg)
    except Exception as err:
        error(err, usr.first_name, usr.id, msg.data)

app.run()