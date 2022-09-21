#!/usr/bin/python3
import discord
from discord.ext import commands
import os
import urllib.request
import asyncio

client = commands.Bot(command_prefix = 'MechaKyle ', owner_id=your_id)
client.remove_command("help")

@client.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title = "Help", description = "Use MechaKyle help <command> for more info on the command.",color = ctx.author.color)

    em.add_field(name = "Kyle only", value = "IP\nload\nunload\nshutdown")
    em.add_field(name = "literally just ping at the moment", value = "ping")

    await ctx.send(embed = em)

@help.command()
async def IP(ctx):

    em = discord.Embed(title = "IP", description = "sends Hobbit IP every change of IP in Hobbits deleting the previous one, to save hassle",color = ctx.author.color)

    em.add_field(name = "**Syntax**", value = "MechaKyle IP")

    await ctx.send(embed = em)

@help.command()
async def ping(ctx):

    em = discord.Embed(title = "ping", description = "some latency command",color = ctx.author.color)

    em.add_field(name = "**Syntax**", value = "MechaKyle ping")

    await ctx.send(embed = em)

@help.command()
async def load(ctx):

    em = discord.Embed(title = "load", description = "load IP cog if it fails or I have to unload it",color = ctx.author.color)

    em.add_field(name = "**Syntax**", value = "MechaKyle load")

    await ctx.send(embed = em)

@help.command()
async def unload(ctx):

    em = discord.Embed(title = "unload", description = "opposite of load",color = ctx.author.color)

    em.add_field(name = "**Syntax**", value = "MechaKyle unload")

    await ctx.send(embed = em)

@help.command()
async def shutdown(ctx):

    em = discord.Embed(title = "shutdown", description = "shut down the bot",color = ctx.author.color)

    em.add_field(name = "**Syntax**", value = "MechaKyle shutdown")

    await ctx.send(embed = em)

@client.event
async def on_ready():
    print("Ayy! MechaKyle's back, real Kyle!")
    await client.change_presence(activity=discord.Activity(name='you!', type=3))
    channel = client.get_channel(905638285202849822)
    amount=1
    variable = 0
    x = 1
    while x:
        ip = urllib.request.urlopen('https://v4.ident.me').read().decode('utf8')
        if variable==ip:
            variable = ip
            await asyncio.sleep(60)
        else:
            await channel.purge(limit=amount)
            ip = urllib.request.urlopen('https://v4.ident.me').read().decode('utf8')
            em = discord.Embed(title = "Hobbit IP is:", description = "This is the IP")
            em.add_field(name = "IP: "+ip, value = "Port: 25565(Bedrock is 19132)")
            await channel.send(embed = em)
            variable = ip
            await asyncio.sleep(60)

        try:
            response=urllib.request.urlopen('http://74.125.131.94/',timeout=1)
            return True
        except urllib.request.URLError as err: pass
        return False
        await client.close()

@client.command()
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(pass_context = True)
@commands.is_owner()
async def shutdown(ctx):
    await client.close()


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('token')
