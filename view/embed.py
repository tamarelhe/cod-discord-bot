import discord
from constants import *
import view.embed_struct as es


E_COLOR = 0xFF5733

async def send_base_embed(ctx, embed_struct):

    if embed_struct.title != '':
        title = TITLE_FRAME_L+embed_struct.title+TITLE_FRAME_R
    else:
        title =  ''

    embed=discord.Embed(title=title, description=embed_struct.description, color=E_COLOR) 

    if embed_struct.attach:
        f = discord.File(embed_struct.attach.path+embed_struct.attach.filename, filename=embed_struct.attach.filename)
        embed.set_image(url="attachment://"+embed_struct.attach.filename)  

    
    for field in embed_struct.fields:
        embed.add_field(name=field.key, value=field.value, inline=field.inline)
    

    embed.set_footer(text=FOOTER)
    
    if embed_struct.attach:
        await ctx.send(embed=embed, file=f)
    else:
        await ctx.send(embed=embed)


async def send_multiple_embeds(ctx, embed_struct, pag_size):

    splitted_fields = []
    new_embed_struct = embed_struct

    for i, field in enumerate(embed_struct.fields):
        splitted_fields.append(field)
        if (i+1)%pag_size == 0:
            new_embed_struct.fields = splitted_fields
            await send_base_embed(ctx, new_embed_struct)
            splitted_fields.clear()

    if len(splitted_fields) > 0:
        new_embed_struct.fields = splitted_fields
        await send_base_embed(ctx, new_embed_struct)