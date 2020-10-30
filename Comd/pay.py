import discord
from discord.ext import commands
from importlib import import_module

class Pay(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["передать"])
    async def pay(self, ctx, member: discord.Member, num: int):
        am = import_module("database")
        data = am.stat(ctx.message.author.id)
        if data["money"] < num:
            await ctx.send("У вас нет столько")
        else:
            am.pays(ctx.message.author.id, member.id, num)
            await ctx.message.add_reaction("✅")

    @pay.error
    async def Pay_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Am")

def setup(client):
    client.add_cog(Pay(client))