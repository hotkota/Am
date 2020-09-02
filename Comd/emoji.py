import discord
from discord.ext import commands

class Emoji(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["emoji"])
    async def эмоция(self, ctx, emoji: discord.Emoji):
        emb = discord.Embed(title = f"{emoji.name}", colour = discord.Color.red())
        emb.set_image(url = emoji.url)
        await ctx.send(embed = emb)

def setup(client):
    client.add_cog(Emoji(client))