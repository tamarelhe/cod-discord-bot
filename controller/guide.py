from constants import *
import model.guide as model
from view.embed import send_base_embed
import view.embed_struct as es
        
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
    fields = []   
    await send_base_embed(ctx, es.EStruct('City Hall', '', es.Attach(GUIDE_ASSETS, 'city_hall_requirements.jpg'), fields))



async def present_cod_media(ctx):
    medias = model.list_all_media()

    fields = []   
    for category in medias:
        media = model.get_media_by_category(category) 
        for m in media:
            fields.append(es.Field(m['description'], m['URL'], True))

    await send_base_embed(ctx, es.EStruct('Media', '', None, fields))
