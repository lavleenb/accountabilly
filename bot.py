import discord

intents = discord.Intents.all()
client = discord.Client(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    print('{0.user} connected to discord!'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('hi'):
        await message.channel.send("hey!")
    
    if message.content.startswith('how are you'):
        await message.channel.send("i'm great!")



client.run("filler")