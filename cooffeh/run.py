from Modules.menu import Callbacks, Commands, Own
from Modules.setup import app, admin
from Shared import tools, message

@app.on_callback_query()
async def callback(client, msg):
    usr = msg.from_user
    actions = Callbacks()
    try:
        call = tools.getCommand(msg.data)
        for c in actions.menu:
            if call[1] == c.command:
                return await c.action(msg, int(call[0]), call[1])
        if 'sites' in call[1]:
            return await actions.sites(msg, call[1])
        return await actions.navigate(msg, int(call[0]), call[1])
    except Exception as err:
        return await app.send_message(admin,
            message.logerr(usr.id, usr.first_name, err, msg.data))

@app.on_message()
async def main(cliente, msg):
    usr = msg.from_user
    await app.send_message(admin,
        message.loginfo(usr.id, usr.first_name, msg.text))
    try:
        lower = msg.text.lower()
        if "youtu.be" in lower or "www.youtube.com" in lower:
            lower = 'youtube'
        elif "instagram.com" in lower and 'scontent.cdninsta' not in lower:
            lower = 'instagram'
        elif 'qrcode' in lower:
            lower = 'qrcode'
        elif 'xsearch' in lower.split(' ')[0]:
            lower = 'xsearch'
        elif 'msearch' in lower.split(' ')[0]:
            lower = 'msearch'
        elif 'search' in lower.split(' ')[0]:
            lower = 'search'

        for commmand in Commands().menu:
            if commmand.command == lower:
                await msg.reply(message.process)
                return await commmand.action(msg)

        if usr.id == admin:
            for commmand in Own().menu:
                if commmand.command == lower:
                    await msg.reply(message.process)
                    return await commmand.action(msg)

    except Exception as err:
        return await app.send_message(admin,
            message.logerr(usr.id, usr.first_name, err, msg.text))

app.run()
