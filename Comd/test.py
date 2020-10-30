import random
import discord
from discord.ext import commands

class Test(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["test", "Test", "Тест"])
    async def тест(self, ctx, *, arg):
        emb = discord.Embed(title = "Проверка",colour = discord.Color.red())
        emb.description = f"{arg} на **{random.randint(0, 100)}**% шизоид"
        await ctx.send(embed = emb)

    @тест.error
    async def Test_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            emb = discord.Embed(title = "Проверка",colour = discord.Color.red())
            emb.description = f"{ctx.message.author.mention} на **{random.randint(0, 100)}**% шизоид"
            await ctx.send(embed = emb)

def setup(client):
    client.add_cog(Test(client))