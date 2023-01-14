from Modules.menu import Callbacks, Commands
from Modules.logger import info, error
from Modules.setup import app
from Shared import tools, message
    
@app.on_callback_query()
async def callback(client, msg):
    usr = msg.from_user
    info(usr.first_name, usr.id, msg.data)
    try:
        call = tools.getCommand(msg.data)
        for c in Callbacks().menu:
            if call[1] == c.command:
                return await c.action(msg, int(call[0]))
    except Exception as err:
        error(err, usr.first_name, usr.id, msg.data)

@app.on_message()
async def main(cliente, msg):
    usr = msg.from_user
    info(usr.first_name, usr.id, msg.text)
    try:
        lower = msg.text.lower()
        if "youtu.be" in lower or "www.youtube.com" in lower:
            lower = 'youtube'
        elif "instagram.com" in lower and 'scontent.cdninstagram.com' not in lower:
            lower = 'instagram'
        elif 'qrcode' in lower:
            lower = 'qrcode'
        elif 'https://' in lower or 'http://' in lower:
            lower = 'videomp4'

        for commmand in Commands().menu:
            if commmand.command == lower:
                await msg.reply(message.process)
                return await commmand.action(msg)
    except Exception as err:
        error(err, usr.first_name, usr.id, msg.text)

app.run()