import discord

intents = discord.Intents.all()
client = discord.Client(command_prefix="<3", intents=intents)

@client.event
async def on_ready():
    print('{0.user} connected to discord!'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('hi'):
        await message.channel.send("hey!")

    if message.content.startswith('pfp'):
        await message.channel.send(file=discord.File('leiu.png'))


client.run('MTA4NDMzMTY5NjQxOTI1ODM4OA.G0rjYX.ItoohKDFW1tfplRMfR7MDURclESAPY9a3c1Aiw')