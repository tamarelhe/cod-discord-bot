import model.artifact as model
from constants import *
from view.embed import send_base_embed, send_multiple_embeds
import view.embed_struct as es
        
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

    fields = []

    for i, id in enumerate(artifacts):
        artifact = model.get_artifact(id)
        fields.append(es.Field(artifact['name'], id, True))

    await send_multiple_embeds(ctx, es.EStruct('Artifacts List', '', None, fields), 14)


async def present_artifact(ctx, id):
    artifact = model.get_artifact(id)

    fields = []
    
    fields.append(es.Field("Info", artifact['info'], False))
    fields.append(es.Field("Tier", artifact['tier'], False))
    fields.append(es.Field("Rarity", artifact['rarity'], False))
    fields.append(es.Field("Role", artifact['role'], False))
    fields.append(es.Field("Stats", artifact['stats'], False))
    fields.append(es.Field("Cooldown", artifact['cooldown'], False))

    await send_base_embed(ctx, es.EStruct(artifact['name'], '', es.Attach(ARTIFACTS_ASSETS, artifact['image']), fields))

        

