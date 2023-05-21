from constants import *
from view.embed import send_base_embed
import view.embed_struct as es
        
async def execute_help_command(ctx, *args):
    if len(args) > 0:
        await ctx.send('Invalid parameter number.')
        return
    
    await present_help(ctx)


async def present_help(ctx):

    fields = []
    
    fields.append(es.Field(TITLE_FRAME_L+"Help", '', False))
    fields.append(es.Field(BOT_PREFIX+'help', 'For retrieve help menu', False))

    fields.append(es.Field(TITLE_FRAME_L+"Hero", '', False))
    fields.append(es.Field(BOT_PREFIX+'hero list', 'For retrieve heroes list', False))
    fields.append(es.Field(BOT_PREFIX+'hero <hero_name>', 'For retrieve hero information', False))
    fields.append(es.Field(BOT_PREFIX+'hero <hero_name> talent_trees', 'For retrieve hero talent trees', False))
    fields.append(es.Field(BOT_PREFIX+'hero <hero_name> artifacts', 'For retrieve hero artifacts', False))
    fields.append(es.Field(BOT_PREFIX+'hero role <role_name>', 'For retrieve heroes by role', False))
    fields.append(es.Field(BOT_PREFIX+'hero unit <unit_type>', 'For retrieve heroes by unit type', False))

    fields.append(es.Field(TITLE_FRAME_L+"Behemoth", '', False))
    fields.append(es.Field(BOT_PREFIX+'behemoth list', 'For retrieve behemoth list', False))
    fields.append(es.Field(BOT_PREFIX+'behemoth <behemoth_name>', 'For retrieve behemoth information', False))

    fields.append(es.Field(TITLE_FRAME_L+"Artifacts", '', False))
    fields.append(es.Field(BOT_PREFIX+'artifact list', 'For retrieve artifacts list', False))
    fields.append(es.Field(BOT_PREFIX+'artifact <artifact_id>', 'For retrieve artifact information', False))

    fields.append(es.Field(TITLE_FRAME_L+"Guides", '', False))
    fields.append(es.Field(BOT_PREFIX+'guide city_hall', 'For retrieve city hall requirements', False))
    fields.append(es.Field(BOT_PREFIX+'guide media', 'For retrieve some guides about COD', False))

    fields.append(es.Field(TITLE_FRAME_L+"Credits", '', False))
    fields.append(es.Field(BOT_PREFIX+'credits', 'For retrieve BOT & Content credits', False))

    await send_base_embed(ctx, es.EStruct('Help Menu', '', es.Attach(BOT_ASSETS, 'cod.jpg'), fields))
    