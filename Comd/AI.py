import discord
import requests
from json import loads
from discord.ext import commands

class AI(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["ии"])
    async def ai(self, ctx, *, arg):
        url = "https://some-random-api.ml/chatbot?message={}".format(arg)
        res = requests.get(url = url)
        json_data = loads(res.text)
        await ctx.send(json_data["response"])

    @ai.error
    async def AI_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Am")

def setup(client):
    client.add_cog(AI(client))