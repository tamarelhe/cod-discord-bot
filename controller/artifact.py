import discord
import model.artifact as model
from constants import *
from disputils import BotEmbedPaginator
        
async def execute_artifact_command(ctx, *args):
    if len(args) != 1:
        await ctx.send('Invalid parameter number.')
        return
    
    match args[0]:
        case 'list':                              
            await present_all_artifacts(ctx)
        case _:
            check = model.get_artifact(args[0])
            if check is None:
                await ctx.send('Artifact '+args[0]+' does not exists.')
                return
            await present_artifact(ctx, args[0])



async def present_all_artifacts(ctx):
    artifacts = model.list_all_artifacts()
    
    embeds = []
    embed=discord.Embed(title=TITLE_FRAME_L+"Artifacts List"+TITLE_FRAME_R, description="\u200B", color=0xFF5733) 
    for i, id in enumerate(artifacts):
        artifact = model.get_artifact(id)        
        embed.add_field(name='Name', value=artifact['name'], inline=True)
        if (i+1)%2 == 0:
            embed.add_field(name="\u200B", value="\u200B")

        if (i+1)%14 == 0:
            embed.add_field(name="\u200B", value="\u200B", inline=True)
            embed.set_footer(text=FOOTER)
            embeds.append(embed)
            embed=discord.Embed(title=TITLE_FRAME_L+"Artifacts List"+TITLE_FRAME_R, description="\u200B", color=0xFF5733)
    embed.add_field(name="\u200B", value="\u200B", inline=False)
    embed.set_footer(text=FOOTER)
    embeds.append(embed)

    paginator = BotEmbedPaginator(ctx, embeds)
    await paginator.run()    


async def present_artifact(ctx, id):
    artifact = model.get_artifact(id)
    
    f = discord.File(ARTIFACTS_ASSETS+artifact['image'], filename=artifact['image'])
    embed=discord.Embed(title=TITLE_FRAME_L+artifact['name']+TITLE_FRAME_R, description="", color=0xFF5733)    
    embed.set_image(url="attachment://"+artifact['image'])  
    embed.add_field(name="Info", value=artifact['info'], inline=False)
    embed.add_field(name="Tier", value=artifact['tier'], inline=True)
    embed.add_field(name="\u200B", value="\u200B", inline=True)
    embed.add_field(name="Rarity", value=artifact['rarity'], inline=True)
    embed.add_field(name="Role", value=artifact['role'], inline=True)
    embed.add_field(name="\u200B", value="\u200B", inline=True)
    embed.add_field(name="Stats", value=artifact['stats'], inline=True)
    embed.add_field(name="Cooldown", value=artifact['cooldown'], inline=True)
    embed.set_footer(text=FOOTER)
    await ctx.send(embed=embed, file=f)
        

