import discord
from constants import *
import model.guide as model
from disputils import BotEmbedPaginator
        
async def execute_guide_command(ctx, *args):
    if len(args) != 1:
        await ctx.send('Invalid parameter number.')
        return
    
    if len(args) == 1:        
        match args[0]:
            case 'city_hall':
                await present_city_hall_requirements(ctx)
            case 'media':
                await present_cod_media(ctx)
            case _:
                await ctx.send(args[1]+': Invalid command option.')
                return

async def present_city_hall_requirements(ctx):    
    f = discord.File(GUIDE_ASSETS+'city_hall_requirements.jpg', filename='city_hall_requirements.jpg')
    embed=discord.Embed(title=TITLE_FRAME_L+"City Hall"+TITLE_FRAME_R, description="\u200B", color=0xFF5733) 
    embed.set_image(url="attachment://"+'city_hall_requirements.jpg') 
    #embed.add_field(name="\u200B", value="\u200B", inline=False)
    embed.set_footer(text=FOOTER)
    await ctx.send(embed=embed, file=f)

async def present_cod_media(ctx):
    medias = model.list_all_media()
    
    list = '\n' 

    for i, category in enumerate(medias):
        media = model.get_media_by_category(category) 

        list = list + '\n**'+category+'**\n\n'

        for m in media:
            list = list + "["+m['description']+"]("+m['URL']+")\n"

    embed=discord.Embed(title=TITLE_FRAME_L+"Media List"+TITLE_FRAME_R, description=list, color=0xFF5733)
    embed.set_footer(text=FOOTER)
    await ctx.send(embed=embed)