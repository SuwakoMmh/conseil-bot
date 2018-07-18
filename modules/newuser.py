import settings.newuser
import discord
import asyncio
async def addrole(client, member):
    if len(member.roles) == 1 :
        await client.add_roles(member, discord.utils.get(member.server.roles, id=settings.newuser.newuserroleid))
async def initscan(client):
    for member in client.get_all_members() :
        if len(member.roles) == 1:
            await client.add_roles(member, discord.utils.get(member.server.roles, id=settings.newuser.newuserroleid))

async def giveroleMessage(client, message):
    if message.content=="/membre" :
        try:
            await client.add_roles(message.author, discord.utils.get(message.author.server.roles, id=settings.newuser.rulesroleid))
            await asyncio.sleep(1)
            await client.remove_roles(message.author, discord.utils.get(message.author.server.roles, id=settings.newuser.newuserroleid))
        except:
            found=False
            for member in client.get_all_members():
                if str(member.id) == str(message.author.id) :
                    try:
                        await client.add_roles(member, discord.utils.get(member.server.roles, id=settings.newuser.rulesroleid))
                        await asyncio.sleep(1)
                        await client.remove_roles(member, discord.utils.get(member.server.roles, id=settings.newuser.newuserroleid))
                        found=True
                    except:
                        pass
            if not found:
                raise

async def giveroleReact(client, reaction, user, action):
    print(str(reaction.custom_emoji))
    print(str(reaction.emoji.name))
    print("olol")
    if reaction.custom_emoji :
        if reaction.emoji.name.lower()=='lumagreen':
            try:
                await client.add_roles(user, discord.utils.get(user.server.roles, id=settings.newuser.rulesroleid))
                await asyncio.sleep(1)
                await client.remove_roles(user, discord.utils.get(user.server.roles, id=settings.newuser.newuserroleid))
            except:
                found=False
                for member in client.get_all_members():
                    if str(member.id) == str(user.id) :
                        try:
                            await client.add_roles(member, discord.utils.get(member.server.roles, id=settings.newuser.rulesroleid))
                            await asyncio.sleep(1)
                            await client.remove_roles(member, discord.utils.get(member.server.roles, id=settings.newuser.newuserroleid))
                            found=True
                        except:
                            pass
                if not found:
                    raise
