import discord
from constants import *
from view.embed import send_base_embed
import view.embed_struct as es
        
async def execute_credits_command(ctx, *args):
    if len(args) > 0:
        await ctx.send('Invalid parameter number.')
        return
    
    await present_credits(ctx)

async def present_credits(ctx):

    fields = []   
    fields.append(es.Field(TITLE_FRAME_L+"Youtubers", '', False))
    fields.append(es.Field('Chisgule Gaming', '[Youtube](https://www.youtube.com/@HulksdenGaming)', True))
    fields.append(es.Field('Hulksden Gaming', '[Youtube](https://www.youtube.com/@Chisgule)', True))

    fields.append(es.Field(TITLE_FRAME_L+"Websites", '', False))
    fields.append(es.Field('Call of Dragons Guides', '[Call of Dragons Guides](https://callofdragonsguides.com/)', True))
    fields.append(es.Field('COD.guide', '[COD.guide](https://cod.guide/)', True))

    await send_base_embed(ctx, es.EStruct('Credits', 'All the content of this bot was taken from the following sources', es.Attach(BOT_ASSETS, 'cod.jpg'), fields))
