import discord
from discord.ext import commands
import urllib.request
import asyncio

class Ip(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def IP(self, ctx, amount=1):
        variable = 0
        x = 1
        ip = urllib.request.urlopen('https://v4.ident.me').read().decode('utf8')
        await ctx.channel.purge(limit=amount)
        await ctx.send("Hobbit IP is: "+ip+":25566")
        while x:
            ip = urllib.request.urlopen('https://v4.ident.me').read().decode('utf8')
            if variable==ip:
                variable = ip
                await asyncio.sleep(1800)
            else:
                await ctx.channel.purge(limit=amount)
                ip = urllib.request.urlopen('https://v4.ident.me').read().decode('utf8')
                await ctx.send("Hobbit IP is: "+ip+":25566")
                variable = ip
                await asyncio.sleep(1800)

def setup(client):
    client.add_cog(Ip(client))
