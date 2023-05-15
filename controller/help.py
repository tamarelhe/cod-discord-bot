import discord
from constants import *
        
async def execute_help_command(ctx, *args):
    if len(args) > 0:
        await ctx.send('Invalid parameter number.')
        return
    
    await present_help(ctx)

async def present_help(ctx):
    commands_help = '''
    '''+BOT_PREFIX+'''help
    '''
    descriptions_help = '''
    For retrieve help menu
    '''

    commands_hero = '''
    '''+BOT_PREFIX+'''hero list
    '''+BOT_PREFIX+'''hero <hero_name>
    '''+BOT_PREFIX+'''hero <hero_name> talent_trees
    '''+BOT_PREFIX+'''hero <hero_name> artifacts
    '''
    descriptions_hero = '''
    For retrieve heroes list
    For retrieve hero information
    For retrieve hero talent trees
    For retrieve hero artifacts
    '''

    commands_behemoth = '''
    '''+BOT_PREFIX+'''behemoth list
    '''+BOT_PREFIX+'''behemoth <behemoth_name>
    '''
    descriptions_behemoth = '''
    For retrieve behemoth list
    For retrieve behemoth information
    '''

    commands_guides = '''
    '''+BOT_PREFIX+'''guide city_hall
    '''+BOT_PREFIX+'''guide media
    '''
    descriptions_guides = '''
    For retrieve city hall requirements
    For retrieve some guides about COD
    '''

    commands_artifacts = '''
    '''+BOT_PREFIX+'''artifact list
    '''+BOT_PREFIX+'''artifact <artifact_id>
    '''
    descriptions_artifacts = '''
    For retrieve artifacts list
    For retrieve artifact information
    '''

    commands_credits = '''
    '''+BOT_PREFIX+'''credits
    '''
    descriptions_credits = '''
    For retrieve BOT & Content credits
    '''

    f = discord.File(BOT_ASSETS+'cod.jpg', filename='cod.jpg')
    embed=discord.Embed(title=TITLE_FRAME_L+"Help Menu"+TITLE_FRAME_R, description="\u200B", color=0xFF5733) 
    embed.set_image(url="attachment://"+'cod.jpg') 
    embed.add_field(name=TITLE_FRAME_L+"Help", value='', inline=False)
    embed.add_field(name="Commands", value=commands_help, inline=True)
    embed.add_field(name="Description", value=descriptions_help, inline=True)
    #embed.add_field(name="\u200B", value="\u200B", inline=False)
    embed.add_field(name=TITLE_FRAME_L+"Hero", value='', inline=False)
    embed.add_field(name="Commands", value=commands_hero, inline=True)
    embed.add_field(name="Description", value=descriptions_hero, inline=True)
    #embed.add_field(name="\u200B", value="\u200B", inline=False)
    embed.add_field(name=TITLE_FRAME_L+"Behemoth", value='', inline=False)
    embed.add_field(name="Commands", value=commands_behemoth, inline=True)
    embed.add_field(name="Description", value=descriptions_behemoth, inline=True)
    #embed.add_field(name="\u200B", value="\u200B", inline=False)
    embed.add_field(name=TITLE_FRAME_L+"Guides", value='', inline=False)
    embed.add_field(name="Commands", value=commands_guides, inline=True)
    embed.add_field(name="Description", value=descriptions_guides, inline=True)
    #embed.add_field(name="\u200B", value="\u200B", inline=False)
    embed.add_field(name=TITLE_FRAME_L+"Artifacts", value='', inline=False)
    embed.add_field(name="Commands", value=commands_artifacts, inline=True)
    embed.add_field(name="Description", value=descriptions_artifacts, inline=True)
    #embed.add_field(name="\u200B", value="\u200B", inline=False)
    embed.add_field(name=TITLE_FRAME_L+"Credits", value='', inline=False)
    embed.add_field(name="Commands", value=commands_credits, inline=True)
    embed.add_field(name="Description", value=descriptions_credits, inline=True)
    

    #embed.add_field(name="\u200B", value="\u200B", inline=False)
    embed.set_footer(text=FOOTER)
    await ctx.send(embed=embed, file=f)