from requests import get
from json import loads
import discord
from discord.ext import commands

res = get("https://some-random-api.ml/img/cat")
json_data = loads(res.text)
embed = discord.Embed(color = 0xd7342a, title = "Кот!")
embed.set_image(url = json_data["link"])

class Cat(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["cat", "Cat", "Кот"])
    async def кот(self, ctx, *, arg):
        if arg == "?":
            emb = discord.Embed(title = 'Команда "/кот"', colour = discord.Color.red())
            emb.description = "Отправляет случайное фото кота"
            await ctx.send(embed = emb)
        else:
            await ctx.send(embed = embed)

    @кот.error
    async def Cat_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed = embed)

def setup(client):
    client.add_cog(Cat(client))