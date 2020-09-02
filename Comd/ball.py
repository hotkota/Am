from random import choice
import discord
from discord.ext import commands

class Ball(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["Шар", "ball", "8Ball"])
    async def шар(self, ctx, *, arg):
        if arg[0] == "?":
            emb = discord.Embed(title = 'Команда "/Шар"',colour = discord.Color.red())
            emb.description = "Отвечает на заданый вопрос"
            await ctx.send(embed = emb)
        else:
            message = ["Да","Нет","Возможно"]
            s = choice(message)
            await ctx.send(s)

    @шар.error
    async def Ball_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Задай мне вопрос")

def setup(client):
    client.add_cog(Ball(client))