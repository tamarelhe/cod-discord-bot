import discord
from discord.ext import commands

from apikeys import *
from controller.hero import execute_hero_command

client = commands.Bot(command_prefix = '$', intents=discord.Intents.all())

heroes_data = None

@client.event
async def on_ready():
    global heroes_data
    print("COD Bot is up and running!")
    print('--------------------------')

@client.command()
async def hero(ctx, *args):
    await execute_hero_command(ctx, *args)

client.run(BOTTOKEN)
