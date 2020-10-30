import discord
from discord.ext import commands
from importlib import import_module

class Up(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def up(self, ctx, *, arg: int):
        if ctx.message.author.id in [540887870941167617, 547437284606214145]:
        	am = import_module("database")
        	am.up(ctx.message.author.id, arg)
        	await ctx.message.add_reaction("✅")
        else:
        	await ctx.message.add_reaction("❌")

def setup(client):
    client.add_cog(Up(client))