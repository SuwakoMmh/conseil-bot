import settings.newuser
import discord
async def addrole(client, member):
    print(member.roles)
    if len(member.roles) == 1 :
        await client.add_roles(member, discord.utils.get(member.server.roles, id=settings.newuser.newuserroleid))
async def initscan(client):
    for member in client.get_all_members() :
        print(member.roles)
        if len(member.roles) == 1:
            await client.add_roles(member, discord.utils.get(member.server.roles, id=settings.newuser.newuserroleid))

async def giveroleMessage(client, message):
    if message.content=="/membre" :
        try:
            client.remove_roles(message.author, discord.utils.get(message.author.server.roles, id=settings.newuser.newuserroleid))
            client.add_roles(message.author, discord.utils.get(message.author.server.roles, id=settings.newuser.rulesroleid))
        except:
            found=False
            for member in client.get_all_members():
                if str(member.id) == str(message.author.id) :
                    try:
                        client.remove_roles(message.author, discord.utils.get(message.author.server.roles, id=settings.newuser.newuserroleid))
                        client.add_roles(message.author, discord.utils.get(message.author.server.roles, id=settings.newuser.rulesroleid))
                        found=True
                    except:
                        pass
            if not found:
                raise
async def giveroleReact(client, reaction, user, action):
    pass
