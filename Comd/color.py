import discord
from discord.ext import commands

class Color(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["color"])
    async def цвет(self, ctx, *, arg):
        emb = discord.Embed(colour = discord.Color.red(), title = f"Цвет {arg}")
        emb.set_image(url = "https://some-random-api.ml/canvas/colorviewer?hex={}".format(arg))
        await ctx.send(embed = emb)

    @цвет.error
    async def Color_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Am")

def setup(client):
    client.add_cog(Color(client))