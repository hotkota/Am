import discord
from json import loads
from requests import get
from discord.ext import commands

res = get("https://some-random-api.ml/img/dog")
json_data = loads(res.text)
embed = discord.Embed(color = 0xd7342a, title = "Dog!")
embed.set_image(url = json_data["link"])

class Dog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["dog", "Dog", "Пес"])
    async def пес(self, ctx, * , arg):
        if arg == "?":
            emb = discord.Embed(title = 'Команда "/пес"', colour = discord.Color.red())
            emb.description = "Отправляет случайное фото собаки"
            await ctx.send(embed = emb)
        else:
            await ctx.send(embed = embed)

    @пес.error
    async def Dog_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed = embed)

def setup(client):
    client.add_cog(Dog(client))