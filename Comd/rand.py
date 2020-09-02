from random import randint
import discord
from discord.ext import commands

emb = discord.Embed(title = 'Команда "/ранд"',colour = discord.Color.red())
emb.description = "Возращает случайное целое число указаное 1 параметром"
emb.add_field(name = "Пример 1:", value = "`/ранд 100`\n\tВернет число от 0 до 100")
emb.add_field(name = "Пример 2:", value = "`/ранд 100 200`\n\tВернет число от 100 до 200")

class Rand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["рандом", "rand", "random"])
    async def ранд(self, ctx, *args):
        if len(args) == 1:
            await ctx.send(randint(0, int(args[0])))
        elif len(args) == 2:
            await ctx.send(randint(int(args[0]), int(args[1])))
        elif len(args) >= 3:
            await ctx.send(embed = emb)
        elif args[0] == "?":
            await ctx.send(embed = emb)
        else:
            await ctx.send(embed = emb)

    @ранд.error
    async def Rand_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send(embed = emb)

def setup(client):
    client.add_cog(Rand(client))