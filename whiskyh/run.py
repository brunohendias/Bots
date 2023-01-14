from Modules.menu import com, Callbacks, Commands
from Modules.logger import info, error, debug
from Modules.setup import app
    
@app.on_callback_query()
async def callback(client, msg):
    usr = msg.from_user
    info(usr.first_name, usr.id, msg.data)
    try:
        m = msg.data.split('_')
        for c in Callbacks().menu:
            if m[1] == c.command:
                return await c.action(msg)
    except Exception as err:
        error(err, usr.first_name, usr.id, msg.data)

@app.on_message()
async def message(cliente, msg):
    usr = msg.from_user
    info(usr.first_name, usr.id, msg.text)
    try:
        lower = msg.text.lower()
        if "youtu.be" in lower or "www.youtube.com" in lower:
            lower = com.youtube
        elif "instagram.com" in lower and 'scontent.cdninstagram.com' not in lower:
            lower = com.instagram
        elif 'qrcode' in lower:
            lower = com.qrcode
        elif 'https://' in lower or 'http://' in lower:
            lower = com.videomp4

        for commmand in Commands().menu:
            if commmand.command == lower:
                return await commmand.action(msg)
    except Exception as err:
        error(err, usr.first_name, usr.id, msg.data)

app.run()