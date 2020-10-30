import discord
from discord.ext import commands
from importlib import import_module

class About(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["about"])
    async def осебе(self, ctx, *, arg):
        am = import_module("database")
        am.desc(ctx.message.author.id, arg)
        await ctx.message.add_reaction("✅")

    @осебе.error
    async def About_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Напишите что нибудь о себе")

def setup(client):
    client.add_cog(About(client))