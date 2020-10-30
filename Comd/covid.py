import discord
from json import loads
from requests import get
from discord.ext import commands

class Covid(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["covid"])
    async def ковид(self, ctx):
        res = loads(get("https://covid19api.com/summary").text)["Global"]
        emb = discord.Embed(color = discord.Color.red(), title = "Ковид")
        emb.add_field(name = "Зараженый", value = f'Новых: **{res["NewConfirmed"]}**\nВсего: **{res["TotalConfirmed"]}**')
        emb.add_field(name = "Выздоровших", value = f'Новых: {res["NewRecovered"]}\nВсего: {res["TotalRecovered"]}')
        emb.add_field(name = "Смертей", value = f'Новых: {res["NewDeaths"]}\nВсего: {res["TotalDeaths"]}')
        await ctx.send(embed = emb)

def setup(client):
    client.add_cog(Covid(client))