import discord
from discord.ext import commands
import os
from dotenv import load_dotenv # used to load environment files
from discord_slash import SlashCommand
# from import 

# import command libraries
from Commands.commands import Cmd
from Commands.slashCommands import Scmd

client = commands.Bot(command_prefix = 's!', activity=discord.Activity(type=discord.ActivityType.watching, name="your health"))
discordClient = discord.Client()
slash = SlashCommand(client, sync_commands=True)
cmd = Cmd()
scmd = Scmd()

@client.event
async def on_ready():
    # print('You are logged in as {0.user}'.format(client))
    print('thump thump')

@client.event
async def on_message(message):

    # process the commands within the discord messages
    await client.process_commands(message)

    # if message.author == client.user:
    #     print("Talking to the author!")
    #     return

    # commands start with "solar"
    # if message.content.startswith('/solar'):
    #     await message.channel.send('Hello!')


##############################  Commands  ######################################
@client.command()
async def about(ctx):
    await ctx.send(cmd.about())

@client.command()
async def signup(ctx):
    await ctx.send(cmd.signUpMessage(str(ctx.author)))
    # userid = await discordClient.get_user_info(ctx.author.id)
    await ctx.message.author.send("Hello! It's Solar here :)")

###########################  Slash Commands  ###################################
@slash.slash(description="Shows the bots latency")
async def signup(ctx):
    await ctx.send(f'Bot Speed - {round(client.latency * 1000)}ms')

##########################  Load Discord Bot  ##################################
load_dotenv('token.env') # load the token environment
client.run(os.getenv('DISCORD_TOKEN')) # run discord client with token
        
