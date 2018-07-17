async def print_user(client):
    print('''\n Bienvenue @''' + client.user.name + "#" + client.user.discriminator)
    print('-------')
