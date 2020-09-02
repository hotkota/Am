import discord
from discord.ext import commands

class Avatar(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["avatar", "Avatar", "Аватар"])
    async def аватар(self, ctx, *, arg: int):
        avamember = await self.client.fetch_user(arg)
        emb = discord.Embed(title = f"Аватар {avamember.name}", colour = discord.Color.red())
        emb.set_image(url = avamember.avatar_url)
        await ctx.send(embed = emb)
    
    @commands.command(aliases = ["avatar", "Avatar", "Аватар"])
    async def аватар(self, ctx, *, avamember: discord.Member):
        emb = discord.Embed(title = f"Аватар {avamember.name}", colour = discord.Color.red())
        emb.set_image(url = avamember.avatar_url)
        await ctx.send(embed = emb)

    @аватар.error
    async def Avatar_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            emb = discord.Embed(title = f"Аватар {ctx.message.author.name}", colour = discord.Color.red())
            emb.set_image(url = ctx.message.author.avatar_url)
            await ctx.send(embed = emb)

def setup(client):
    client.add_cog(Avatar(client))