import discord
from constants import *
        
async def execute_credits_command(ctx, *args):
    if len(args) > 0:
        await ctx.send('Invalid parameter number.')
        return
    
    await present_credits(ctx)

async def present_credits(ctx):
    
    f = discord.File(BOT_ASSETS+'cod.jpg', filename='cod.jpg')
    embed=discord.Embed(title=TITLE_FRAME_L+"Credits"+TITLE_FRAME_R, description="All the content of this bot was taken from the following sources\u200B", color=0xFF5733) 
    embed.set_image(url="attachment://"+'cod.jpg') 

    embed.add_field(name=TITLE_FRAME_L+"Youtubers", value='', inline=False)
    embed.add_field(name='Chisgule Gaming', value='[Youtube](https://www.youtube.com/@HulksdenGaming)', inline=False)
    embed.add_field(name='Hulksden Gaming', value='[Youtube](https://www.youtube.com/@Chisgule)', inline=False)

    embed.add_field(name=TITLE_FRAME_L+"Websites", value='', inline=False)
    embed.add_field(name='Call of Dragons Guides', value='[Call of Dragons Guides](https://callofdragonsguides.com/)', inline=False)
    embed.add_field(name='COD.guide', value='[COD.guide](https://cod.guide/)', inline=False)

    embed.set_footer(text=FOOTER)
    await ctx.send(embed=embed, file=f)