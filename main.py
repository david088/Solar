import discord
import os
from dotenv import load_dotenv # used to load environment files

client = discord.Client()

@client.event
async def on_ready():
    print('You are logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        print("Talking to the author!")
        return

    # commands start with "solar"
    if message.content.startswith('$solar'):
        await message.channel.send('Hello!')

load_dotenv('token.env') # load the token environment
client.run(os.getenv('DISCORD_TOKEN')) # run discord client with token
        
