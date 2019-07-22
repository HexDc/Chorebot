# -*- coding: utf-8 -*-    
import os
from discord.ext import commands
import discord
import sys
import os
import config
prefix = [
    ';'
]

description = ';clist'
#insert your database address
link = 'https://raw.githubusercontent.com/HexDc/EmotMachine/master/data/'
bot = commands.Bot(command_prefix=prefix, description=description)


@bot.command(hidden=False)
async def clist(ctx):
    embed = discord.Embed(title="**List of Emoticons**", description=config.descript, color=0xffffff) 
    await ctx.send(embed=embed)
@bot.command(hidden=False)
async def c1(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")
    embed.set_image(url=link + "1.png")
    await ctx.send(embed=embed)
    
