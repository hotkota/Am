import discord
from json import loads
from requests import get
from discord.ext import commands

res = get("https://some-random-api.ml/img/fox")
json_data = loads(res.text)
embed = discord.Embed(color = 0xd7342a, title = "Лиса!")
embed.set_image(url = json_data["link"])

class Fox(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["fox", "Fox", "Лиса"])
    async def лиса(self, ctx, *, arg):
        if arg == "?":
            emb = discord.Embed(title = 'Команда "/лиса"', colour = discord.Color.red())
            emb.description = "Отправляет случайное фото лисы"
            await ctx.send(embed = emb)
        else:
            await ctx.send(embed = embed)

    @лиса.error
    async def Fox_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed = embed)

def setup(client):
    client.add_cog(Fox(client))