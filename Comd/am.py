import discord
from discord.ext import commands

class Am(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["am"])
    async def ам(self, ctx, *, arg):
        if arg[0] == "?":
            await ctx.send("Am?")
        else:
            await ctx.send("Am")

    @ам.error
    async def Am_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Am")

def setup(client):
    client.add_cog(Am(client))