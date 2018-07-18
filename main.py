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
@client.event
async def on_message(message):
    if settings.restart.enabled:
        await modules.restart.restart_py(client, message)
    if settings.newuser.enabled:
        await modules.newuser.giveroleMessage(client, message)
@client.event
async def on_member_join(member):
    if settings.newuser.enabled:
        await modules.newuser.addrole(client,member)
@client.event
async def on_error(event, *args, **kwargs):
    if settings.embederror.enabled :
        await modules.embederror.sendError(client, event, *args, **kwargs)
@client.event
async def on_reaction_add(reaction, user):
    if settings.newuser.enabled:
        await modules.newuser.giveroleReact(client, reaction, user, 'add')
client.run(os.environ['CONSEIL_TOKEN'])
