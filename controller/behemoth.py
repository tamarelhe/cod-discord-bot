import discord
import model.behemoth as model
from constants import *
from disputils import BotEmbedPaginator
        
async def execute_behemoth_command(ctx, *args):
    if len(args) != 1:
        await ctx.send('Invalid parameter number.')
        return
    
    match args[0]:
        case 'list':                              
            await present_all_behemoths(ctx)
        case _:
            check = model.get_behemoth(args[0])
            if check is None:
                await ctx.send('Behemoth '+args[0]+' does not exists.')
                return
            await present_behemoth(ctx, args[0])



async def present_all_behemoths(ctx):
    behemoths = model.list_all_behemoths()
    
    embeds = []
    embed=discord.Embed(title=TITLE_FRAME_L+"Behemoths List"+TITLE_FRAME_R, description="\u200B", color=0xFF5733) 
    for i, name in enumerate(behemoths):
        behemoth = model.get_behemoth(name)        
        embed.add_field(name='Name', value=name, inline=True)
        if (i+1)%2 == 0:
            embed.add_field(name="\u200B", value="\u200B")

        if (i+1)%14 == 0:
            embed.add_field(name="\u200B", value="\u200B", inline=True)
            embed.set_footer(text=FOOTER)
            embeds.append(embed)
            embed=discord.Embed(title=TITLE_FRAME_L+"Behemoths List"+TITLE_FRAME_R, description="\u200B", color=0xFF5733)
    embed.add_field(name="\u200B", value="\u200B", inline=False)
    embed.set_footer(text=FOOTER)
    embeds.append(embed)

    paginator = BotEmbedPaginator(ctx, embeds)
    await paginator.run()    


async def present_behemoth(ctx, name):
    behemoth = model.get_behemoth(name)
    
    f = discord.File(BEHEMOTHS_ASSETS+behemoth['image'], filename=behemoth['image'])
    embed=discord.Embed(title=TITLE_FRAME_L+name+TITLE_FRAME_R, description="", color=0xFF5733)    
    embed.set_image(url="attachment://"+behemoth['image'])  
    embed.add_field(name="Attack", value=behemoth['attack'], inline=True)
    embed.add_field(name="HP", value=behemoth['hp'], inline=True)
    embed.add_field(name="\u200B", value="\u200B", inline=True)
    embed.add_field(name="Power", value=behemoth['power'], inline=True)
    embed.add_field(name="Defense", value=behemoth['defense'], inline=True)
    embed.add_field(name="\u200B", value="\u200B", inline=True)
    embed.add_field(name="Movement Speed", value=behemoth['movement_speed'], inline=True)
    embed.add_field(name="Battle Duration", value=behemoth['battle_duration'], inline=True)
    embed.add_field(name="\u200B", value="\u200B", inline=False)
    embed.add_field(name="Guides", value="", inline=True)
    for i, url in enumerate(behemoth['urls']):
        embed.add_field(name="", value="["+name+" Guide "+str(i+1)+"]("+url+")", inline=False)
        #embed=discord.Embed(title="", description="["+name+" Behemoth]("+url+")", color=0xFF5733)
    embed.set_footer(text=FOOTER)
    await ctx.send(embed=embed, file=f)
        

