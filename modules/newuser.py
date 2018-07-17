async def addrole(client, member):
    if len(member.roles) == 1 :
        await client.add_roles(member, settings.newuser.roleid)
async def initscan(client):
    for member in client.get_all_members() :
        if len(member.roles) == 1:
            await client.add_roles(member, settings.newuser.roleid)
