import discord
from discord.ext import commands

from apikeys import *
from controller.help import execute_help_command
from controller.hero import execute_hero_command 
from controller.behemoth import execute_behemoth_command 
from controller.guide import execute_guide_command 
from controller.artifact import execute_artifact_command
from controller.credits import execute_credits_command
from constants import *

activity = discord.Game(name=BOT_PREFIX+"help")
client = commands.Bot(command_prefix = BOT_PREFIX, activity=activity, intents=discord.Intents.all())
client.remove_command('help')

heroes_data = None

    

@client.event
async def on_ready():
    global heroes_data
    print("COD Bot is up and running!")
    print('\n------ Server List ------\n')
    async for guild in client.fetch_guilds(limit=150):
        print(guild.name)

@client.command()
async def help(ctx, *args):
    await execute_help_command(ctx, *args)

@client.command()
async def hero(ctx, *args):
    await execute_hero_command(ctx, *args)

@client.command()
async def behemoth(ctx, *args):
    await execute_behemoth_command(ctx, *args)

@client.command()
async def guide(ctx, *args):
    await execute_guide_command(ctx, *args)

@client.command()
async def artifact(ctx, *args):
    await execute_artifact_command(ctx, *args)

@client.command()
async def credits(ctx, *args):
    await execute_credits_command(ctx, *args)

client.run(BOTTOKEN)