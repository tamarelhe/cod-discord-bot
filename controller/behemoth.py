import model.behemoth as model
from constants import *
from view.embed import send_base_embed, send_multiple_embeds
import view.embed_struct as es
        
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
    
    fields = []

    for i, name in enumerate(behemoths):
        behemoth = model.get_behemoth(name)

        fields.append(es.Field(behemoth['name'], '', False))

    await send_multiple_embeds(ctx, es.EStruct('Behemoths List', '', None, fields), 14)


async def present_behemoth(ctx, name):    
    behemoth = model.get_behemoth(name)
    if behemoth is None or not behemoth:
        await ctx.send('There is no behemoth '+name+'.')

    fields = []
    
    fields.append(es.Field("Attack", behemoth['attack'], True))
    fields.append(es.Field("HP", behemoth['hp'], True))
    fields.append(es.Field("\u200B", "\u200B", True))
    fields.append(es.Field("Power", behemoth['power'], True))
    fields.append(es.Field("Defense", behemoth['defense'], True))
    fields.append(es.Field("\u200B", "\u200B", True))
    fields.append(es.Field("Movement Speed", behemoth['movement_speed'], True))
    fields.append(es.Field("Battle Duration", behemoth['battle_duration'], False))
    fields.append(es.Field("Guides [Youtube]", "", False))
    for url in behemoth['urls']:
        fields.append(es.Field('', '['+url['title']+']('+url['url']+')', False))

    await send_base_embed(ctx, es.EStruct(behemoth['name'], '', es.Attach(BEHEMOTHS_ASSETS, behemoth['image']), fields))

        

