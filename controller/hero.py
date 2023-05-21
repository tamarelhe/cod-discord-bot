import discord
import model.hero as model
import model.artifact as model_a
from constants import *
import controller.artifact as arti
from view.embed import send_base_embed, send_multiple_embeds
import view.embed_struct as es
        
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
    
    fields = []

    for i, name in enumerate(heroes):
        hero = model.get_hero(name)

        fields.append(es.Field(name+' ['+hero['rarity']+']', hero['role']+' | '+hero['buffs']+' | '+hero['units'], True))

    await send_multiple_embeds(ctx, es.EStruct('Heroes List', '', None, fields), 14)


async def present_hero(ctx, name):
    hero = model.get_hero(name)

    fields = []
    
    fields.append(es.Field("Rarity", hero['rarity'], True))
    fields.append(es.Field("Role", hero['role'], True))
    fields.append(es.Field("\u200B", "\u200B", True))
    fields.append(es.Field("Buffs", hero['buffs'], True))
    fields.append(es.Field("Units", hero['units'], True))
    fields.append(es.Field("\u200B", "\u200B", True))
    fields.append(es.Field("Pairings", hero['pairings'], True))
    fields.append(es.Field("Tier", hero['tier'], True))
    fields.append(es.Field("\u200B", "\u200B", True))
    for skill in hero['skills']:
        fields.append(es.Field("\u200B", "\u200B", True))
        fields.append(es.Field(skill['name']+' ['+skill['type']+']', skill['description']+'\n'+skill['upgrade_desc'], False))
    fields.append(es.Field("\u200B", "\u200B", False))

    await send_base_embed(ctx, es.EStruct(name, '', es.Attach(HERO_ASSETS, hero['images']['main']), fields))


async def present_hero_talent_trees(ctx, name):
    talent_trees = model.get_hero_talent_trees(name)

    for talent_tree in talent_trees:
        await send_base_embed(ctx, es.EStruct('', '', es.Attach(TALENT_TREES_ASSETS, talent_tree), []))


async def present_hero_artifacts(ctx, name):
    artifacts = model.get_hero_artifacts(name)

    for i, artifact in enumerate(artifacts):
        await arti.present_artifact(ctx, artifact['id'])
