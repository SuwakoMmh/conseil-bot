#!/usr/bin/python3
import discord #pip3 install --user discord[voice]
import asyncio
import os

import settings
import modules
import utils.perms

client = discord.Client(max_messages=100000)
@client.event
async def on_ready():
    if settings.login.enabled:
        await modules.login.print_user(client)
    if settings.newuser.enabled:
        await modules.newuser.initscan(client)

async def on_member_join(member):
    if modules.newuser.enabled:
        await modules.newuser.addrole(client,member)
client.run(os.environ['CONSEIL_TOKEN'])
