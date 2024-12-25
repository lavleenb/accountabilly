import discord
import os
from dotenv import load_dotenv

load_dotenv()
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')

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



client.run(DISCORD_BOT_TOKEN)