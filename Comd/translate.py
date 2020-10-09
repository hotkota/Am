import discord
import googletrans
from discord import File
from discord.ext import commands
from googletrans import Translator

translator = Translator()

class Translate(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["translate", "перевод", "t"])
    async def переводчик(self, ctx, *arg):
        if len(arg) == 0:
            emb = discord.Embed(title = "Ошибка", colour = discord.Color.red())
            emb.description = "Введите язык и текст для перевода"
        else:
            data = translator.translate(" ".join(arg[1:]), dest = arg[0])
            emb = discord.Embed(title = "Перевод", colour = discord.Color.red())
            emb.add_field(name = "Оригинал:", value = data.origin)
            emb.add_field(name = "Вывод:", value = data.text)
        await ctx.send(embed = emb)

def setup(client):
    client.add_cog(Translate(client))