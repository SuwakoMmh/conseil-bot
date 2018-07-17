import settings.restart
import utils.perms
import pygit2
async def restart_py(client, message):
    if (not (message.author == client.user)) and (message.content.startswith("/restart") and await utils.perms.hasrole(message.author, settings.restart.restartAuth) and pygit2.Repository('.').head.shorthand=="master"):
        if str(message.content) == "/restart" :
            try:
                await client.delete_message(message)
            except:
                pass
            await client.send_message(message.channel, message.author.mention + ", Juge Dredd reviendra...")
            await client.logout()
