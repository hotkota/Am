import random
import discord
from discord.ext import commands
from importlib import import_module

cfg = import_module("config").prefix

emb = discord.Embed(color = discord.Color.red(), title = 'Команда "/казино"')
emb.description = "Один из способов тратить деньги"
emb.add_field(name = "Пример:", value = "`/казино 100`\nС некоторым шансов можно получить 200 монет или проиграть 100") 

class Casino(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["casino"])
    async def казино(self, ctx, *, num):
        if num.isdigit():
            num = int(num)
            am = import_module("database")
            data = am.stat(ctx.message.author.id)
            if num <= 0:
                await ctx.send("Ставка не должна быть отрицательной")
            else:
                if data["money"] < num:
                    await ctx.send("У вас нет столько")
                else:
                    shance, shance_2 = random.randint(1, 99), random.randint(1, 50)
                    if shance <= shance_2:
                        am.azino(ctx.message.author.id, num, 1)
                        await ctx.send(f"Вы выйграли и получили {num * 2} монеты")
                    else:
                        am.azino(ctx.message.author.id, num, 0)
                        await ctx.send(f"Вы проиграли и потеряли {num} монеты")
        elif num == "?":
            await ctx.send(embed = emb)
        else:
            await ctx.send("Аргумент не число")

    @казино.error
    async def Casino_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed = emb)

def setup(client):
    client.add_cog(Casino(client))