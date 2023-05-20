import discord
import model.hero as model
import model.artifact as model_a
from constants import *
from disputils import BotEmbedPaginator
import controller.artifact as arti
        
async def execute_hero_command(ctx, *args):
    if len(args) == 0 or len(args) > 2:
        await ctx.send('Invalid parameter number.')
        return
    
    if len(args) == 1:
        match args[0]:
            case 'list':                              
                await present_all_heroes(ctx)
            case _:
                check = model.get_hero(args[0])
                if check is None:
                    await ctx.send('Hero '+args[0]+' does not exists.')
                    return
                await present_hero(ctx, args[0])

    if len(args) == 2:
        check = model.get_hero(args[0])
        if check is None:
            await ctx.send('Hero '+args[0]+' does not exists.')
            return

        match args[1]:
            case 'talent_trees':
                await present_hero_talent_trees(ctx, args[0])
            case 'artifacts':
                await present_hero_artifacts(ctx, args[0])
            case _:
                await ctx.send(args[1]+': Invalid command option.')
                return




async def present_all_heroes(ctx):
    heroes = model.list_all_heroes()
    
    embeds = []
    embed=discord.Embed(title=TITLE_FRAME_L+"Heroes List"+TITLE_FRAME_R, description="\u200B", color=0xFF5733) 
    for i, name in enumerate(heroes):
        hero = model.get_hero(name)
        n = name+' ['+hero['rarity']+']'
        v = hero['role']+' | '+hero['buffs']+' | '+hero['units']
        embed.add_field(name=n, value=v, inline=True)
        if (i+1)%2 == 0:
            embed.add_field(name="\u200B", value="\u200B")

        if (i+1)%14 == 0:
            embed.add_field(name="\u200B", value="\u200B", inline=True)
            embed.set_footer(text=FOOTER)
            embeds.append(embed)
            embed=discord.Embed(title=TITLE_FRAME_L+"Heroes List"+TITLE_FRAME_R, description="\u200B", color=0xFF5733)
    embed.add_field(name="\u200B", value="\u200B", inline=False)
    embed.set_footer(text=FOOTER)
    embeds.append(embed)

    paginator = BotEmbedPaginator(ctx, embeds)
    await paginator.run()    


async def present_hero(ctx, name):
    hero = model.get_hero(name)
    
    f = discord.File(HERO_ASSETS+hero['images']['main'], filename=hero['images']['main'])
    embed=discord.Embed(title=TITLE_FRAME_L+name+TITLE_FRAME_R, description="", color=0xFF5733)    
    embed.set_image(url="attachment://"+hero['images']['main'])  
    embed.add_field(name="Rarity", value=hero['rarity'], inline=True)
    embed.add_field(name="Role", value=hero['role'], inline=True)
    embed.add_field(name="\u200B", value="\u200B", inline=True)
    embed.add_field(name="Buffs", value=hero['buffs'], inline=True)
    embed.add_field(name="Units", value=hero['units'], inline=True)
    embed.add_field(name="\u200B", value="\u200B", inline=True)
    embed.add_field(name="Pairings", value=hero['pairings'], inline=True)
    embed.add_field(name="Tier", value=hero['tier'], inline=True)
    embed.add_field(name="\u200B", value="\u200B", inline=True)
    for skill in hero['skills']:
        embed.add_field(name="\u200B", value="\u200B", inline=True)
        embed.add_field(name=skill['name']+' ['+skill['type']+']', value=skill['description']+'\n'+skill['upgrade_desc'], inline=False)
    embed.add_field(name="\u200B", value="\u200B", inline=False)
    embed.set_footer(text=FOOTER)
    await ctx.send(embed=embed, file=f)



async def present_hero_talent_trees(ctx, name):
    talent_trees = model.get_hero_talent_trees(name)

    for talent_tree in talent_trees:
        f = discord.File(TALENT_TREES_ASSETS+talent_tree, filename=talent_tree)
        embed=discord.Embed(title='', description='', color=0xFF5733)
        embed.set_image(url="attachment://"+talent_tree)
        await ctx.send(embed=embed, file=f)


async def present_hero_artifacts(ctx, name):
    artifacts = model.get_hero_artifacts(name)

    for i, artifact in enumerate(artifacts):
        await arti.present_artifact(ctx, artifact['id'])
