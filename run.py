# -*- coding: utf-8 -*-    
import os
from discord.ext import commands
import discord
import sys
import os
import config
import random
import traceback


tok = config.token

co=0xffffff

link = config.link
bot = commands.Bot(command_prefix=config.prefix, description=config.description)

def __init__(self, bot):
    self.bot = bot
    print('Addon "{}" loaded'.format(self.__class__.__name__))

@bot.command(hidden=False)
async def clist(ctx):
    embed = discord.Embed(title="**List of Emoticons**", description=config.descript, color=0xffffff) 
    await ctx.send(embed=embed)
@bot.command()
async def say(ctx, *, str=""):
    await ctx.message.delete()
    str = str.replace('@everyone', '`@everyone`').replace('@here', '`@here`')
    await ctx.send("{}".format(str))
@bot.command()
async def c1(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "1.png")
    await ctx.send(embed=embed)
@bot.command()
async def c2(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "2.png")
    await ctx.send(embed=embed)
@bot.command()
async def c3(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "3.png")
    await ctx.send(embed=embed)
@bot.command()
async def c4(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "4.png")
    await ctx.send(embed=embed)
@bot.command()
async def c5(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "5.png")
    await ctx.send(embed=embed)
@bot.command()
async def c6(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "6.png")
    await ctx.send(embed=embed)
@bot.command()
async def c7(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "7.png")
    await ctx.send(embed=embed)
@bot.command()
async def c8(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "8.png")
    await ctx.send(embed=embed)
@bot.command()
async def c9(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "9.png")
    await ctx.send(embed=embed)
@bot.command()
async def c10(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "10.png")
    await ctx.send(embed=embed)
@bot.command()
async def c11(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "11.png")
    await ctx.send(embed=embed)
@bot.command()
async def c12(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "12.png")
    await ctx.send(embed=embed)
@bot.command()
async def c13(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "13.png")
    await ctx.send(embed=embed)
@bot.command()
async def c14(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "14.png")
    await ctx.send(embed=embed)
@bot.command()
async def c15(ctx, user:discord.Member=None):
    if not user:
        user = ctx.author
    await ctx.message.delete()
    embed = discord.Embed(title=format(user), description="used emoticon:")

    embed.set_image(url=link + "15.png")
    await ctx.send(embed=embed)

bot.run(tok)
