import discord
from json import loads
from requests import get
from discord.ext import commands

emb = discord.Embed(color = 0xd7342a, title = "Фото")
emb.description = "**Доступные фото**:\nлиса\nкот\nпес\nкоала\nптица"

class Fox(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["foto"])
    async def фото(self, ctx, *, arg):
        arg = arg.lower()
        if arg == "лиса" or arg == "лис":
            res = get("https://some-random-api.ml/img/fox")
            json_data = loads(res.text)
            emb = discord.Embed(color = 0xd7342a, title = "Лиса!")
            emb.set_image(url = json_data["link"])
        elif arg == "пес" or arg == "собака":
            res = get("https://some-random-api.ml/img/dog")
            json_data = loads(res.text)
            emb = discord.Embed(color = 0xd7342a, title = "Пес!")
            emb.set_image(url = json_data["link"])
        elif arg == "кот":
            res = get("https://some-random-api.ml/img/cat")
            json_data = loads(res.text)
            emb = discord.Embed(color = 0xd7342a, title = "Кот!")
            emb.set_image(url = json_data["link"])
        elif arg == "коала":
            res = get("https://some-random-api.ml/img/koala")
            json_data = loads(res.text)
            emb = discord.Embed(color = 0xd7342a, title = "Коала!")
            emb.set_image(url = json_data["link"])
        elif arg == "птица":
            res = get("https://some-random-api.ml/img/birb")
            json_data = loads(res.text)
            emb = discord.Embed(color = 0xd7342a, title = "Птица!")
            emb.set_image(url = json_data["link"])
        await ctx.send(embed = emb)

    @фото.error
    async def Fox_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed = emb)

def setup(client):
    client.add_cog(Fox(client))