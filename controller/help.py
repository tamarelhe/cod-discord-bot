import discord
from constants import *
        
async def execute_help_command(ctx, *args):
    if len(args) > 0:
        await ctx.send('Invalid parameter number.')
        return
    
    await present_help(ctx)

async def present_help(ctx):

    f = discord.File(BOT_ASSETS+'cod.jpg', filename='cod.jpg')
    embed=discord.Embed(title=TITLE_FRAME_L+"Help Menu"+TITLE_FRAME_R, description="\u200B", color=0xFF5733) 
    embed.set_image(url="attachment://"+'cod.jpg') 
    
    embed.add_field(name=TITLE_FRAME_L+"Help", value='', inline=False)
    embed.add_field(name=BOT_PREFIX+'help', value='For retrieve help menu', inline=True)
    
    embed.add_field(name=TITLE_FRAME_L+"Hero", value='', inline=False)
    embed.add_field(name=BOT_PREFIX+'hero list', value='For retrieve heroes list', inline=False)
    embed.add_field(name=BOT_PREFIX+'hero <hero_name>', value='For retrieve hero information', inline=False)
    embed.add_field(name=BOT_PREFIX+'hero <hero_name> talent_trees', value='For retrieve hero talent trees', inline=False)
    embed.add_field(name=BOT_PREFIX+'hero <hero_name> artifacts', value='For retrieve hero artifacts', inline=False)

    embed.add_field(name=TITLE_FRAME_L+"Behemoth", value='', inline=False)
    embed.add_field(name=BOT_PREFIX+'behemoth list', value='For retrieve behemoth list', inline=False)
    embed.add_field(name=BOT_PREFIX+'behemoth <behemoth_name>', value='For retrieve behemoth information', inline=False)

    embed.add_field(name=TITLE_FRAME_L+"Artifacts", value='', inline=False)
    embed.add_field(name=BOT_PREFIX+'artifact list', value='For retrieve artifacts list', inline=False)
    embed.add_field(name=BOT_PREFIX+'artifact <artifact_id>', value='For retrieve artifact information', inline=False)

    embed.add_field(name=TITLE_FRAME_L+"Guides", value='', inline=False)
    embed.add_field(name=BOT_PREFIX+'guide city_hall', value='For retrieve city hall requirements', inline=False)
    embed.add_field(name=BOT_PREFIX+'guide media', value='For retrieve some guides about COD', inline=False)

    embed.add_field(name=TITLE_FRAME_L+"Credits", value='', inline=False)
    embed.add_field(name=BOT_PREFIX+'credits', value='For retrieve BOT & Content credits', inline=False)
    
    embed.set_footer(text=FOOTER)
    await ctx.send(embed=embed, file=f)